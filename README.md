> 📌 **Môn học:** Trí tuệ nhân tạo  
> 📌 **Loại bài:** Đồ án báo cáo cuối kì  
> 📌 **Thuật toán:** A* (A-Star Search)

---
# 🧠 PHẦN 1. THUẬT TOÁN A*
## 🔷 1.1. Giới thiệu

Thuật toán **A\*** (*A-Star Search*) là một thuật toán tìm kiếm đường đi tối ưu trong đồ thị có trọng số, được sử dụng rộng rãi trong lĩnh vực **Trí tuệ nhân tạo**, đặc biệt trong các bài toán tìm đường, định tuyến và lập kế hoạch.

Mục tiêu của thuật toán là tìm **đường đi có tổng chi phí nhỏ nhất** từ một đỉnh bắt đầu đến một đỉnh đích.

---

## 🔷 1.2. Nguyên lý hoạt động

Thuật toán A\* sử dụng một **hàm đánh giá** để lựa chọn đỉnh mở rộng tiếp theo:

\[
f(n) = g(n) + h(n)
\]

Trong đó:

- 🟦 **g(n)**: chi phí thực tế từ đỉnh bắt đầu đến đỉnh \( n \)  
- 🟧 **h(n)**: chi phí ước lượng từ đỉ
