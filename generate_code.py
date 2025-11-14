import ollama


prompt = """Write only valid Python code for a bubble sort function that sorts a list in ascending order without using sorted() or sort() functions.

Requirements:
- Only output Python code, no explanations or markdown
- No code blocks or backticks
- Include the complete function definition
- Make it production-ready and well-commented
- Function name must be 'bubble_sort'
- Function should modify the list in-place

Start coding now:"""
a = ollama.generate(model="codellama:7b", prompt=prompt)

ai_code = a['response']
file_name = "sort_list.py"
with open(file_name, "w") as f:
    f.write(ai_code)

