<h2>Agent实验<h2>
<h3>题目要求<h3>
实现一个只需要使用语言即可使用的选课系统，不包含任何GUI。被调用的函数可以使用copilot生成，不需要使用数据库，只需要能够模拟对应功能。

功能简介
查询：带有筛选的查询，可以筛选必修或选修。
选课：选择需要的课程，智能返回结果
成功返回选课结果
未成功返回错误
删除：删除选择的课程，智能返回结果
进阶要求
查询增强，根据描述返回用户最为感兴趣的课程
例如：用户喜欢体育，羽毛球等放在前面
选择增强：当用户在选课和删除时提供的课程不准确时，智能提供可能用户想提的课程
实验资源
python 库：https://github.com/QwenLM/Qwen-Agent
调用模型的设置可以参考如下：