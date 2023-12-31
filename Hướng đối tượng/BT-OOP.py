import tkinter as tk
from tkinter import messagebox

class EmployeeManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quản lý nhân viên")

        # Tạo các biến lưu thông tin
        self.employee_data = []
        self.load_data_from_file()

        # Tạo các label và entry widgets
        self.label = tk.Label(root, text="Thông tin nhân viên")
        self.label.pack(fill=tk.BOTH, expand=True)

        self.employee_id_label = tk.Label(root, text="Mã số:")
        self.employee_id_label.pack(fill=tk.BOTH, expand=True)
        self.employee_id_entry = tk.Entry(root)
        self.employee_id_entry.pack(fill=tk.BOTH, expand=True)

        self.employee_name_label = tk.Label(root, text="Họ tên:")
        self.employee_name_label.pack(fill=tk.BOTH, expand=True)
        self.employee_name_entry = tk.Entry(root)
        self.employee_name_entry.pack(fill=tk.BOTH, expand=True)

        self.employee_salary_label = tk.Label(root, text="Mức lương:")
        self.employee_salary_label.pack(fill=tk.BOTH, expand=True)
        self.employee_salary_entry = tk.Entry(root)
        self.employee_salary_entry.pack(fill = tk.BOTH, expand=True)

        self.employee_department_ID_label = tk.Label(root, text="Mã phòng ban:")
        self.employee_department_ID_label.pack(fill=tk.BOTH, expand=True)
        self.employee_department_ID_entry = tk.Entry(root)
        self.employee_department_ID_entry.pack(fill = tk.BOTH, expand=True)

        self.employee_department_label = tk.Label(root, text="Tên phòng ban:")
        self.employee_department_label.pack(fill=tk.BOTH, expand=True)
        self.employee_department_entry = tk.Entry(root)
        self.employee_department_entry.pack(fill = tk.BOTH, expand=True)

        # Tạo các nút chức năng
        self.add_button = tk.Button(root, text="Thêm nhân viên", command=self.add_employee)
        self.add_button.pack(fill = tk.BOTH, expand=True)

        self.remove_button = tk.Button(root, text="Loại bỏ nhân viên", command=self.remove_employee)
        self.remove_button.pack(fill = tk.BOTH, expand=True)

        self.increase_salary_button = tk.Button(root, text="Tăng lương", command=self.increase_salary)
        self.increase_salary_button.pack(fill = tk.BOTH, expand=True)


        self.list_button = tk.Button(root, text="Liệt kê nhân viên", command=self.list_employees)
        self.list_button.pack(fill = tk.BOTH, expand=True) 

        self.save_button = tk.Button(root, text="Lưu danh sách", command=self.save_data_to_file)
        self.save_button.pack(fill = tk.BOTH, expand=True)

        self.exit_button = tk.Button(root, text="Thoát", command=root.quit)
        self.exit_button.pack(fill = tk.BOTH, expand=True)

    def add_employee(self):
        employee_id = self.employee_id_entry.get()
        employee_name = self.employee_name_entry.get()
        employee_salary = self.employee_salary_entry.get()
        employee_department_ID = self.employee_department_ID_entry.get()
        employee_department = self.employee_department_entry.get()
        
        # Kiểm tra xem mã số đã tồn tại hay chưa
        for emp in self.employee_data:
            if emp['Mã số'] == employee_id:
                messagebox.showerror("Lỗi", "Mã số nhân viên đã tồn tại")
                return
        
        new_employee = {
            'Mã số': employee_id,
            'Họ tên': employee_name,
            'Mức lương': employee_salary,
            'Mã phòng ban': employee_department_ID,
            'Tên phòng ban': employee_department
        }
        self.employee_data.append(new_employee)
        self.clear_entries()
        self.list_employees()

    def remove_employee(self):
        employee_id = self.employee_id_entry.get()
        
        for emp in self.employee_data:
            if emp['Mã số'] == employee_id:
                self.employee_data.remove(emp)
                self.clear_entries()
                self.list_employees()
                return

        messagebox.showerror("Lỗi", "Không tìm thấy nhân viên với mã số này")

    def increase_salary(self):
        employee_id = self.employee_id_entry.get()
        salary_increase = self.employee_salary_entry.get()

        for emp in self.employee_data:
            if emp['Mã số'] == employee_id:
                emp['Mức lương'] = str(float(emp['Mức lương']) + float(salary_increase))
                self.clear_entries()
                self.list_employees()
                return

        messagebox.showerror("Lỗi", "Không tìm thấy nhân viên với mã số này")

    def list_employees(self):
        list_window = tk.Toplevel(self.root)
        list_window.title("Danh sách nhân viên")
        list_window.geometry("+50+100")
        for emp in self.employee_data:
            emp_info = f"Mã số: {emp['Mã số']}, Họ tên: {emp['Họ tên']}, Mức lương: {emp['Mức lương']}, Mã phòng ban: {emp['Mã phòng ban']}, Tên phòng ban: {emp['Tên phòng ban']}"
            label = tk.Label(list_window, text=emp_info)
            label.pack(fill=tk.BOTH, expand=True)

    def save_data_to_file(self):
        with open("NV.txt", "w", encoding='utf-8') as file:
            for emp in self.employee_data:
                emp_info = f"{emp['Mã số']};{emp['Họ tên']};{emp['Mức lương']};{emp['Mã phòng ban']};{emp['Tên phòng ban']}\n"
                file.write(emp_info)

    def load_data_from_file(self):
        try:
            with open("NV.txt", "r", encoding="utf-8") as file:
                for line in file:
                    employee_info = line.strip().split(";")
                    employee = {
                        'Mã số': employee_info[0],
                        'Họ tên': employee_info[1],
                        'Mức lương': employee_info[2],
                        'Mã phòng ban': employee_info[3],
                        'Tên phòng ban': employee_info[4]
                    }
                    self.employee_data.append(employee)
        except FileNotFoundError:
            # Handle the case where the file doesn't exist
            pass


    def clear_entries(self):
        self.employee_id_entry.delete(0, tk.END)
        self.employee_name_entry.delete(0, tk.END)
        self.employee_salary_entry.delete(0, tk.END)
        self.employee_department_ID_entry.delete(0, tk.END)
        self.employee_department_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    root.minsize(400, 400)
    root.geometry("+700+200")
    app = EmployeeManagementApp(root)
    root.mainloop()
