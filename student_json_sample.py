import json
import os

# --- 1. PREPARE DATA STRUCTURE ---
dataset = {
    "company": "TechCorp",
    "established": 2018,
    "employees": [
        {
            "id": 101,
            "name": "John Doe",
            "department": "Engineering",
            "skills": ["Python", "SQL", "Docker"],
            "salary": 75000.00,
            "is_remote": True,
        },
        {
            "id": 102,
            "name": "Alice Walk",
            "department": "Data Science",
            "skills": ["Python", "Pandas", "PyTorch"],
            "salary": 92000.00,
            "is_remote": False,
        },
    ],
}

file_path = "company_data.json"


# --- 2. WRITE TO JSON FILE (DEVELOPMENT / SAVING) ---
def save_json_file(path: str, data: dict):
    try:
        with open(path, "w", encoding="utf-8") as f:
            # indent=4 formats the output clearly with spacing
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"[SUCCESS]: data saved to '{path}'.")
    except IOError as err:
        print(f"[ERROR]: failed to write file '{err}'")


# --- 3. READ AND PARSE JSON FILE ---
def read_json_file(path: str) -> dict:
    if not os.path.exists(path):
        raise FileNotFoundError(f"Target file missing '{path}'")

    try:
        with open(path, "r", encoding="UTF-8") as f:
            content = json.load(f)
            return content
    except json.JSONDecodeError as err:
        print(f"[ERROR]: Invalid JSON Format in '{path}': {err}")
        return {}


# --- 4. UPDATE AND MODIFY JSON CONTENT ---
def amend_employee(path: str, new_employee: dict) -> None:
    data = read_json_file(path)
    if data:
        data["employees"].append(new_employee)
        save_json_file(path, data)


# --- 5. EXECUTION ---
if __name__ == "__main__":
    # 1. CREATE FILE
    save_json_file(file_path, dataset)

    # 2. READ BACK AND OUTPUT SPECIFIC VALUES
    current_data = read_json_file(file_path)
    print(f"First Employee Name: {current_data["employees"][0]["name"]}")

    # 3. APPEND A NEW RECORD AND UPDATE FILE
    new_hire = {
        "id": 103,
        "name": "Robert Chen",
        "department": "DevOps",
        "skills": ["AWS", "Kubernetes"],
        "salary": 88000.00,
        "is_remote": True,
    }

    new_hire2 = {
        "id": 104,
        "name": "Mohsin Azmi",
        "department": "Python",
        "skills": ["Python", "SQL"],
        "salary": 90000.00,
        "is_remote": True,
    }
    amend_employee(file_path, new_hire)
    amend_employee(file_path, new_hire2)
