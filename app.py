import random
import streamlit as st
import pandas as pd
import os

# 获取当前脚本的目录
script_dir = os.path.dirname(os.path.abspath(__file__))

# 加载数据
try:
    data = pd.read_json(os.path.join(script_dir, "tiku.json"))
    worse_list = pd.read_csv(os.path.join(script_dir, "worse_list.csv"), encoding="gbk")
except Exception as e:
    st.error(f"加载数据时出错：{e}")
    st.stop()


# 初始化会话状态
def initialize_session_state():
    default_values = {
        "submit": False,
        "selected_page": "随机题目",
        "worse": worse_list["题号"].values.tolist() if not worse_list.empty else [],
        "current_question": None,
        "user_choice": None,
        "search_query": 1,
    }
    for key, value in default_values.items():
        if key not in st.session_state:
            st.session_state[key] = value


initialize_session_state()

# 设置页面配置
st.set_page_config(page_title="2024毛概题库选择题", layout="wide", page_icon="🏫")

# 设置标题
st.title("2024毛概题库选择题")

# 侧边栏菜单
with st.sidebar:
    menu = ["随机题目", "选看某题", "错题集"]
    selected_page = st.selectbox("在这选择页面~", menu)
    st.markdown("---\n**基于学校给的题库**\n有bug跟我说一下捏，我改一改~")


# 定义加载新题目的函数
def load_new_question(random_mode=True):
    if random_mode:
        random_id = random.choice(data["题号"].unique())
    else:
        random_id = st.session_state.search_query
    question = data[data["题号"] == random_id].iloc[0]
    st.session_state["current_question"] = question
    st.session_state["submit"] = False
    st.session_state["user_choice"] = None


# 定义将错题添加到错题集的函数
def add_to_worse(question):
    if question["题号"] not in st.session_state["worse"]:
        st.session_state["worse"].append(question["题号"])
        st.success("已加入错题集。")
    else:
        st.info("该题已在错题集中。")


# 定义显示题目和处理逻辑的函数
def display_question():
    if st.session_state["current_question"] is not None:
        current_question = st.session_state["current_question"]

        st.markdown(f"## {current_question['题号']}: {current_question['题目']}")

        options = [f"{chr(65 + i)}. {opt}" for i, opt in enumerate(current_question["选项"])]
        radio_key = f"radio_{current_question['题号']}"

        if current_question["题型"] == "单选题":
            user_choice = st.radio(
                f"难度 {current_question['难度']} | 请选择一个选项",
                options,
                key=radio_key,
                disabled=st.session_state["submit"],
            )
        else:
            user_choice = st.multiselect(
                f"难度 {current_question['难度']} | 此题为多选题，请选择所有正确的选项",
                options,
                default=st.session_state["user_choice"] or [],
                key=radio_key,
                disabled=st.session_state["submit"],
            )

        if not st.session_state["submit"] and user_choice != st.session_state["user_choice"]:
            st.session_state["user_choice"] = user_choice

        # 提交按钮
        if st.button("提交", disabled=st.session_state["submit"]):
            st.session_state["submit"] = True
            check_answer(current_question, user_choice)

        # 下一题按钮
        if st.button("下一题"):
            load_new_question(random_mode=(selected_page == "随机题目"))
            st.experimental_rerun()
    else:
        st.info("点击上方的按钮来加载一个题目。")


# 检查答案
def check_answer(question, user_choice):
    correct_answer = question["正确答案"]
    if question["题型"] == "单选题":
        correct_letter = correct_answer.strip()[0]
        selected_letter = user_choice[0]
        is_correct = selected_letter == correct_letter
    else:
        correct_answers = [ans.strip() for ans in correct_answer.split('.') if ans]
        selected_answers = [choice.split('.')[0] for choice in user_choice]
        is_correct = set(selected_answers) == set(correct_answers)

    if is_correct:
        st.success("回答正确！")
    else:
        st.error(f"回答错误！正确答案是：{correct_answer}")
        if st.button("加入错题集"):
            add_to_worse(question)

    if question.get("解析") and question["解析"] != "试题解析":
        st.info(f"答案解析：{question['解析']}")


# 主体内容
if selected_page == "随机题目":
    col1, _ = st.columns([1, 1])
    if col1.button("开始随机~"):
        load_new_question(random_mode=True)
        st.experimental_rerun()
    display_question()

elif selected_page == "选看某题":
    temp_query = st.number_input(
        label="请输入一个整数 1-225",
        min_value=1,
        max_value=225,
        value=st.session_state["search_query"],
        step=1,
        format="%d",
    )
    if temp_query != st.session_state["search_query"]:
        st.session_state["search_query"] = temp_query
    if st.button("查看题目"):
        load_new_question(random_mode=False)
        st.experimental_rerun()
    display_question()

elif selected_page == "错题集":
    st.header("错题集")
    if st.session_state["worse"]:
        worse_df = data[data["题号"].isin(st.session_state["worse"])]
        st.dataframe(worse_df)
        if st.button("保存错题集"):
            worse_df.to_csv(os.path.join(script_dir, "worse_list.csv"), index=False)
            st.success("错题集已保存。")
    else:
        st.info("您的错题集目前为空。")
