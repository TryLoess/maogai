import random
import streamlit_antd_components as sac
import streamlit as st
import pandas as pd
import os

# 获取当前脚本的目录
script_dir = os.path.dirname(os.path.abspath(__file__))

# 加载数据
data = pd.read_json(os.path.join(script_dir, "tiku.json"))
worse_list = pd.read_csv(os.path.join(script_dir, "worse_list.csv"), encoding="gbk")

# 初始化会话状态
if "submit" not in st.session_state:
    st.session_state.submit = False
if "selected_page" not in st.session_state:
    st.session_state.selected_page = "随机题目"
if "worse" not in st.session_state:
    if not worse_list.empty:
        st.session_state.worse = worse_list["题号"].values.to_list()
    else:
        st.session_state.worse = []

if "current_question" not in st.session_state:
    st.session_state.current_question = None
if "user_choice" not in st.session_state:
    st.session_state.user_choice = None
if "search_query" not in st.session_state:
    st.session_state.search_query = 1

# 设置页面配置
st.set_page_config(page_title="2024毛概题库选择题", layout="wide", page_icon="🏫")

# 设置标题
st.title("2024毛概题库选择题")

# 侧边栏菜单
with st.sidebar:
    selected_page = sac.menu(
        [
            sac.MenuItem("随机题目"),
            sac.MenuItem("选看某题"),
            sac.MenuItem("错题集")
        ],
        key="selected_page",
        open_index=0,
    )

    sac.divider()
    st.markdown("**基于学校给的题库**\n有bug跟我说一下捏，我改一改")

# 定义加载新题目的函数
def load_new_question(random_mode=True):
    if random_mode:
        random_id = random.choice(data["题号"].unique())  # 随机选择一个题号
    else:
        # 用于“选看某题”模式，按顺序或特定逻辑加载题目
        random_id = st.session_state.search_query
    question = data[data["题号"] == random_id].iloc[0]
    st.session_state.current_question = question
    st.session_state.submit = False
    st.session_state.user_choice = None

# 定义将错题添加到错题集的函数
def add_to_worse(question):
    # 检查错题是否已经存在于错题集
    existing_ids = [q['题号'] for q in st.session_state.worse]
    if question['题号'] not in existing_ids:
        st.session_state.worse.append(question.to_dict())
        st.success("已加入错题集。")
    else:
        st.info("该题已在错题集中。")

# 定义显示题目和处理逻辑的函数
def display_question():
    if st.session_state.current_question is not None:
        current_question = st.session_state.current_question

        # 显示题目和难度
        st.markdown(f"""## {current_question["题号"]}:{current_question['题目']}""")

        # 构建选项列表
        options = [f"{chr(65 + i)}. {opt}" if opt[1] != "." else opt for i, opt in enumerate(current_question["选项"])]

        # 为每个题目设置唯一的键，以保存用户选择
        radio_key = f"radio_{current_question['题号']}"

        # 根据题型显示单选或多选组件，并禁用选择
        if current_question["题型"] == "单选题":
            user_choice = st.radio(
                f"难度 {current_question['难度']}|请选择一个选项",
                options,
                key=radio_key,
                index=0 if st.session_state.user_choice is None else (
                    options.index(st.session_state.user_choice) if st.session_state.user_choice in options else 0
                ),
                disabled=st.session_state.submit  # 禁用选择
            )
            if not st.session_state.submit and user_choice != st.session_state.user_choice:
                st.session_state.user_choice = user_choice
                st.experimental_rerun()
        else:
            # 多选题使用 multiselect
            user_choice = st.multiselect(
                f"难度 {current_question['难度']}|此题为多选题，请选择所有正确的选项",
                options,
                default=st.session_state.user_choice or [],
                key=radio_key,
                disabled=st.session_state.submit  # 禁用选择
            )
            if not st.session_state.submit and user_choice != st.session_state.user_choice:
                st.session_state.user_choice = user_choice
                st.experimental_rerun()

        # 创建按钮布局，使按钮在同一行
        btn_col1, btn_col2 = st.columns([1, 11])

        # 提交按钮，仅在未提交时显示
        if not st.session_state.submit:
            if btn_col1.button("提交"):
                st.session_state.submit = True

        # 处理提交逻辑
        if st.session_state.submit:
            correct_answer = current_question["正确答案"]
            if current_question["题型"] == "单选题":
                # 假设正确答案是单个字母，例如 'A'
                correct_letter = correct_answer.strip()[0]
                selected_letter = st.session_state.user_choice[0]  # 选项的第一个字符
                is_correct = selected_letter == correct_letter
            else:
                correct_answers = [ans.strip() for ans in correct_answer.split('.')][:-1]
                selected_answers = [choice.split('.')[0] for choice in st.session_state.user_choice]
                is_correct = set(selected_answers) == set(correct_answers)

            if is_correct:
                st.success("回答正确！")
            else:
                st.error(f"回答错误！正确答案是：{current_question['正确答案']}")
                # 提供将错题加入错题集的按钮
                if st.button("加入错题集"):
                    add_to_worse(current_question)

            # 显示答案解析
            if current_question["解析"] and current_question["解析"] != "试题解析":
                st.info(f"答案解析：{current_question['解析']}")

        # 下一题按钮
        if btn_col2.button("下一题"):
            if selected_page == "随机题目":
                load_new_question(random_mode=True)
            elif selected_page == "选看某题":
                load_new_question(random_mode=False)
                # 如果是“选看某题”，更新搜索查询
                st.session_state.search_query += 1
                if st.session_state.search_query > 225:  # 防止溢出
                    st.session_state.search_query = 1
            st.experimental_rerun()
    else:
        st.info("点击上方的按钮来加载一个题目。")

# 主体内容
if selected_page == "随机题目":
    col1, _ = st.columns([1, 1])

    # 按钮触发加载新题
    if col1.button("开始随机~"):
        load_new_question(random_mode=True)
        st.experimental_rerun()

    # 显示当前题目和相关组件
    display_question()

elif selected_page == "选看某题":
    # 使用一个临时变量存储搜索查询的值
    temp_query = st.number_input(
        label="请输入一个整数1-225",
        min_value=1,
        max_value=225,
        value=st.session_state.search_query,  # 使用当前会话状态的值作为默认值
        step=1,
        format="%d",
    )

    # 将临时值同步回会话状态（在必要时）
    if temp_query != st.session_state.search_query:
        st.session_state.search_query = temp_query

    # 按钮触发加载指定题目
    if st.button("查看题目"):
        load_new_question(random_mode=False)
        st.experimental_rerun()

    # 显示当前题目和相关组件
    display_question()

elif selected_page == "错题集":
    st.header("错题集")
    if st.session_state.worse:
        worse_df = pd.DataFrame(st.session_state.worse)
        st.dataframe(worse_df)
        if st.button("保存错题集"):
            worse_df.to_csv("worse_list.csv", index=False)
    else:
        st.info("您的错题集目前为空。")

