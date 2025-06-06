"""
导入测试脚本
测试各种Python模块的导入情况
"""

def print_separator():
    """打印分隔线"""
    print("=" * 70)

def test_import(module_name):
    """测试导入模块"""
    print(f"尝试导入 {module_name}...", end=" ")
    try:
        __import__(module_name)
        print("成功")
        return True
    except Exception as e:
        print(f"失败: {type(e).__name__}: {e}")
        return False

def main():
    """主函数"""
    print_separator()
    print("Python模块导入测试")
    print_separator()
    
    print("\n基本模块:")
    basic_modules = [
        "os", "sys", "time", "datetime", "math", "random", 
        "json", "csv", "pathlib", "collections"
    ]
    
    for module in basic_modules:
        test_import(module)
    
    print("\n正则表达式相关模块:")
    re_modules = [
        "re", "re._compiler", "re._parser", "re._constants", 
        "sre_compile", "sre_parse", "sre_constants", "_sre"
    ]
    
    for module in re_modules:
        test_import(module)
    
    print("\nGUI相关模块:")
    gui_modules = [
        "tkinter", "tkinter.ttk", "tkinter.font", "tkinter.filedialog",
        "tkinter.messagebox", "tkinter.scrolledtext"
    ]
    
    for module in gui_modules:
        test_import(module)
    
    print("\n项目依赖模块:")
    dependency_modules = [
        "openai", "requests", "docx"
    ]
    
    for module in dependency_modules:
        test_import(module)
    
    print_separator()
    print("测试完成")
    print_separator()
    
    print("""
根据上述测试结果，您可以确定哪些模块可以正常导入，哪些模块存在问题。

如果正则表达式相关模块(re, _sre等)导入失败，但基本模块导入成功，
这表明您的Python安装存在部分问题，但不是完全损坏。

如果GUI相关模块(tkinter等)导入失败，但其他模块正常，
这表明您的Python安装缺少GUI支持，可以使用命令行版本的程序。

如果项目依赖模块(openai, requests, docx)导入失败，
这表明您需要安装这些依赖项: pip install -r requirements.txt
    """)
    
    input("\n按Enter键退出...")

if __name__ == "__main__":
    main()
