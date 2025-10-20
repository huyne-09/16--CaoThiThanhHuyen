# student_manager.py

# Danh sách để lưu thông tin các sinh viên.
# Mỗi sinh viên là một dictionary.
student_list = []

def add_student(name, year_of_birth, address):
    """
    YÊU CẦU 1: Hoàn thiện hàm này.
    - Tạo một dictionary để lưu thông tin sinh viên.
    - Thêm dictionary đó vào danh sách `student_list`.
    - In ra thông báo "Da them sinh  vien <ten> thanh cong."
    """
    ### VIẾT CODE CỦA BẠN VÀO ĐÂY ###
    student = {
        "name": name,
        "year_of_birth": year_of_birth,
        "address": address
    }
    student_list.append(student)
    print(f"Da them sinh vien {name} thanh cong.")

def print_student_list():
    """
    YÊU CẦU 2: Hoàn thiện hàm này.
    - In ra thông tin của tất cả các sinh viên trong `student_list`
      theo định dạng:
      "Ten: <ten>, Nam sinh: <nam_sinh>, Dia chi: <dia_chi>"
    """
    ### VIẾT CODE CỦA BẠN VÀO ĐÂY ###
    for student in student_list:
        print(f"Ten: {student['name']}, Nam sinh: {student['year_of_birth']}, Dia chi: {student['address']}")
    
