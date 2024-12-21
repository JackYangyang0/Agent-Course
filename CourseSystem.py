class CourseSystem:
    def __init__(self):
        # 模拟课程数据
        self.courses = {
            1: {"name": "软件工程管理", "type": "必修", "description": "软件工程基础课程"},
            2: {"name": "数据结构", "type": "必修", "description": "计算机科学基础"},
            3: {"name": "计算机网络", "type": "必修", "description": "计算机科学基础"},
            4: {"name": "羽毛球", "type": "选修", "description": "体育类课程"},
            5: {"name": "乒乓球", "type": "选修", "description": "体育类课程"},
            6: {"name": "古代诗词", "type": "选修", "description": "文学类课程"},
        }

    def list_courses(self):
        return [{"id": cid, **course} for cid, course in self.courses.items()]

    def add_course(self, name, course_type, description):
        # 假设课程ID是基于现有课程数量自动生成的
        new_id = max(self.courses.keys(), default=0) + 1
        self.courses[new_id] = {"name": name, "type": course_type, "description": description}
        return f"成功添加课程: {name}"

    def update_course(self, course_id, name=None, course_type=None, description=None):
        if course_id not in self.courses:
            return f"课程ID {course_id} 不存在。"

        course = self.courses[course_id]
        if name:
            course["name"] = name
        if course_type:
            course["type"] = course_type
        if description:
            course["description"] = description
        return f"成功更新课程: {course['name']}"

    def delete_course_by_name(self, course_name):
        for course_id, course in list(self.courses.items()):
            if course["name"] == course_name:
                del self.courses[course_id]
                return f"成功删除课程: {course_name}"
        return f"未找到名为 {course_name} 的课程。"
