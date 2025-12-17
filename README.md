> 📌 **Môn học:** Trí tuệ nhân tạo  
> 📌 **Loại bài:** Đồ án báo cáo cuối kì  
> 📌 **Thuật toán:** A* (A-Star Search)

---

# 🧠 THUẬT TOÁN A* (A-STAR SEARCH)

## 🔷 1. Giới thiệu

Thuật toán **A\*** (*A-Star Search*) là một thuật toán tìm kiếm đường đi tối ưu trong đồ thị có trọng số. Thuật toán được ứng dụng rộng rãi trong lĩnh vực **Trí tuệ nhân tạo**, đặc biệt trong các bài toán tìm đường, định tuyến và lập kế hoạch.

Mục tiêu của thuật toán là tìm **đường đi có tổng chi phí nhỏ nhất** từ đỉnh bắt đầu đến đỉnh đích.

---

## 🔷 2. Nguyên lý hoạt động

Thuật toán A\* sử dụng hàm đánh giá:

\[
f(n) = g(n) + h(n)
\]

Trong đó:

- 🟦 **g(n)**: chi phí thực tế từ đỉnh bắt đầu đến đỉnh \( n \)  
- 🟧 **h(n)**: chi phí ước lượng từ đỉnh \( n \) đến đỉnh đích  
- 🟥 **f(n)**: tổng chi phí ước lượng của đường đi qua đỉnh \( n \)

Tại mỗi bước, thuật toán sẽ **chọn đỉnh có giá trị \( f(n) \) nhỏ nhất** để mở rộng.

---

## 🔷 3. Các tập trong thuật toán

Thuật toán A\* sử dụng hai tập chính:

- **OPEN list**: tập các đỉnh đã được phát hiện nhưng chưa mở rộng  
- **CLOSED list**: tập các đỉnh đã được mở rộng hoàn toàn  

Quy trình tổng quát:
1. Đưa đỉnh bắt đầu vào OPEN
2. Lặp cho đến khi OPEN rỗng:
   - Chọn đỉnh có \( f(n) \) nhỏ nhất trong OPEN
   - Nếu là đỉnh đích → kết thúc
   - Ngược lại: đưa vào CLOSED và mở các đỉnh kề

---

## 🔷 4. Heuristic sử dụng

Trong đồ án này, heuristic được sử dụng là **khoảng cách Euclid** giữa hai đỉnh:

\[
h(n) = \sqrt{(x_n - x_{goal})^2 + (y_n - y_{goal})^2}
\]

Giá trị heuristic được **làm tròn 2 chữ số thập phân** để dễ theo dõi trong quá trình thực hiện thuật toán.

---

# 🧩 MÔ TẢ BÀI TOÁN

## 🔷 5. Dạng bài toán

- Đồ thị **vô hướng**
- Có **trọng số trên các cạnh**
- Trọng số là **số nguyên dương**

Mục tiêu là tìm đường đi có **tổng trọng số nhỏ nhất** từ đỉnh bắt đầu đến đỉnh kết thúc.

---

## 🔷 6. Dữ liệu đầu vào

Chương trình hỗ trợ **hai cách khởi tạo đồ thị**:

### 🔹 6.1. Sinh đồ thị ngẫu nhiên
- Người dùng nhập số đỉnh \( n \) ( \( 3 \le n \le 10 \) )
- Mỗi đỉnh có **bậc tối thiểu ≥ 2**
- Trọng số cạnh được sinh ngẫu nhiên trong khoảng từ 1 đến 9

### 🔹 6.2. Load đồ thị từ file `.txt`

Định dạng file:

```txt
6
A B C D E F
0 2 0 0 0 0
2 0 3 0 1 0
0 3 0 2 0 0
0 0 2 0 3 2
0 1 0 3 0 2
0 0 0 2 2 0


---

## 🔷 7. Mã giả thuật toán A*

```text
OPEN ← {start}
CLOSED ← ∅
g(start) ← 0

while OPEN không rỗng:
    n ← đỉnh có f(n) nhỏ nhất trong OPEN
    nếu n là goal:
        truy vết và trả về đường đi
    đưa n vào CLOSED
    với mỗi đỉnh kề m của n:
        nếu m ∉ CLOSED:
            tính g mới
            nếu m chưa trong OPEN hoặc g mới nhỏ hơn:
                cập nhật g(m), parent(m)
                đưa m vào OPEN

