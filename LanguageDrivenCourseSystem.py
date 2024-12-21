import json
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from CourseSystem import CourseSystem


class LanguageDrivenCourseSystem:
    def __init__(self, model):
        self.model = model
        self.course_system = CourseSystem()

        # 定义一个处理查询的 Prompt 模板
        self.query_prompt = PromptTemplate(
            input_variables=["query"],
            template="""
            你是一个智能选课助手，用户可以通过自然语言进行选课、查询课程、删除课程等操作。
            请解析以下用户输入，并生成相应的操作指令：
            支持的操作包括：
            1. 列出所有课程
            2. 添加课程
            3. 更新课程
            4. 删除课程

            示例：
            用户输入: "我想添加一门选修课，名字是数据仓库，描述是大数据相关课程"
            输出: {{"action": "add", "name": "数据仓库", "type": "选修", "description": "大数据相关课程"}}

            用户输入: "列出所有课程"
            输出: {{"action": "list"}}

            用户输入: {query}
            请输出格式化后的 JSON，不要输出解释或其他内容。
            """
        )
        self.query_chain = LLMChain(llm=self.model, prompt=self.query_prompt)

    def handle_query(self, user_input):
        try:
            # 使用模型处理用户输入
            action_json = self.query_chain.run({"query": user_input})

            # 安全地解析 JSON 格式的字符串
            action = json.loads(action_json)
            print(f"生成的操作指令：{action}")

            # 检查操作指令是否完整
            if "action" not in action:
                return {"error": "操作指令中缺少 'action' 字段"}

            action_type = action["action"].lower()

            # 根据操作指令调用 CourseSystem 的方法
            if action_type == "list":
                return self.course_system.list_courses()

            elif action_type == "add":
                required_fields = ["name", "type", "description"]
                if not all(field in action for field in required_fields):
                    return {"error": "添加课程时缺少必要字段: 'name', 'type', 'description'"}
                return self.course_system.add_course(
                    name=action["name"],
                    course_type=action["type"],
                    description=action["description"]
                )

            elif action_type == "update":
                if "id" not in action:
                    return {"error": "更新课程时缺少 'id' 字段"}
                return self.course_system.update_course(
                    course_id=action["id"],
                    name=action.get("name"),
                    course_type=action.get("type"),
                    description=action.get("description")
                )

            elif action_type == "delete":
                if "name" not in action:
                    return {"error": "删除课程时缺少 'name' 字段"}
                return self.course_system.delete_course_by_name(course_name=action["name"])

            else:
                return {"error": "未识别的操作指令"}

        except json.JSONDecodeError:
            return {"error": "解析操作指令失败，返回的不是有效的 JSON 格式"}
        except Exception as e:
            return {"error": "发生未知错误", "details": str(e)}