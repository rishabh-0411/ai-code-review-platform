class PromptBuilder:

    @classmethod
    def build(cls, repository_info, files):

        prompt = f"""
You are a Senior Software Engineer performing a professional code review.

Repository Information:

- Files: {repository_info["files"]}
- Directories: {repository_info["directories"]}
- Languages: {repository_info["languages"]}
- Frameworks: {repository_info["frameworks"]}
- Package Managers: {repository_info["package_managers"]}

Review the following codebase for:

1. Code Quality
2. Architecture
3. Security Issues
4. Performance
5. Maintainability
6. Best Practices

Return ONLY valid JSON in this format:

{{
    "overall_score": 0-10,
    "strengths": [],
    "issues": [],
    "recommendations": []
}}

"""

        for file in files:

            prompt += f"\n\n### FILE: {file['path']}\n"

            prompt += file["content"]

        return prompt