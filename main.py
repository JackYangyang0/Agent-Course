from langchain.llms import OpenAIChat
from LanguageDrivenCourseSystem import LanguageDrivenCourseSystem
import os

if __name__ == "__main__":
    # 初始化语言模型
    os.environ["OPENAI_API_KEY"] = "None"
    os.environ["OPENAI_API_BASE"] = "http://10.58.0.2:8000/v1"
    model = OpenAIChat(model="Qwen2.5-14B")

    # 创建语言驱动的选课系统
    language_system = LanguageDrivenCourseSystem(model)

    while True:
        user_input = input("请输入您的需求（例如：查询所有课程，输入退出或exit即可退出系统）：")

        if user_input.lower() in ["退出", "exit"]:
            break
        response = language_system.handle_query(user_input)
        print("系统回复：", response)
