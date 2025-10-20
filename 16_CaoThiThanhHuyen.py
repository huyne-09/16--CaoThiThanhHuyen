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

def search_student(search_name):
    """
    YÊU CẦU 3: Hoàn thiện hàm này.
    - Tìm kiếm sinh viên theo tên trong `student_list`.
    - Nếu tìm thấy, in ra thông tin của sinh viên đó theo định dạng:
      "Ten: <ten>, Nam sinh: <nam_sinh>, Dia chi: <dia_chi>"
    - Nếu không tìm thấy, in ra thông báo "Khong tim thay sinh vien <ten>."
    """
    ### VIẾT CODE CỦA BẠN VÀO ĐÂY ###
    found = False
    for student in student_list:
        if student['name'] == search_name:
            print(f"Ten: {student['name']}, Nam sinh: {student['year_of_birth']}, Dia chi: {student['address']}")
            found = True
            break
    if not found:
        print(f"Khong tim thay sinh vien {search_name}.")
# --- Phần thực thi chính để kiểm tra ---
# Sinh viên không cần chỉnh sửa phần này.
if __name__ == "__main__":
    print("--- CHUONG TRINH QUAN LY SINH VIEN ---")
    
    # Yêu cầu 1: Thêm sinh viên
    print("\n1. Them sinh vien:")
    add_student("Nguyen Van An", 2003, "Da Nang")
    add_student("Tran Thi Binh", 2002, "Quang Nam")
    add_student("Le Van Hung", 2003, "Hue")

    # Yêu cầu 2: In danh sách
    print("\n2. In danh sach sinh vien:")
    print_student_list()

    # Yêu cầu 3: Tìm kiếm
    print("\n3. Tim kiem sinh vien theo ten 'an':")
    search_student("an")
    
    print("\nTim kiem sinh vien theo ten 'Dung':")
    search_student("Dung")



    
