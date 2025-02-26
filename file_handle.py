import pandas as pd

def read_target_info(path: str = "target/target.xlsx"):
    try:
        # 读取 Excel，确保所有数据以字符串格式读取
        df = pd.read_excel(path, dtype=str)
        # 去除空白行
        df = df.dropna(how="all")
        # 去除列名前后空格，避免列名匹配问题
        df.rename(columns=lambda x: x.strip(), inplace=True)

        # 检查 command 列并设置为空的值为 None
        if 'command' in df.columns:
            df['command'] = df['command'].replace('/', None)  # 将空字符串替换为 None

        # 转换为字典列表
        data_list = df.to_dict(orient="records")
        return data_list

    except FileNotFoundError:
        print(f"错误: 文件 {path} 未找到！")
    except Exception as e:
        print(f"错误: 读取 Excel 文件失败，原因: {e}")

    return []  # 发生异常时返回空列表


def write_to_txt(file_path, content, mode="w", encoding="utf-8"):
    try:
        # 按行去除空白，并过滤掉空行
        lines = content.splitlines()  # 按行拆分
        cleaned_lines = [line.strip() for line in lines if line.strip()]  # 去掉空行和首尾空白
        if not cleaned_lines:  # 避免写入完全为空的内容
            print("⚠️ 仅包含空行，不执行写入！")
            return False

        # 写入文件
        with open(file_path, mode, encoding=encoding) as file:
            file.write("\n".join(cleaned_lines) + "\n")  # 保证正常换行
        return True
    except Exception as e:
        return False



