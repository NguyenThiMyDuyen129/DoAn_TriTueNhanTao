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
```
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
```
---

# ♟️ THUẬT TOÁN MINIMAX & ALPHA–BETA PRUNING

## 🔷 8. Giới thiệu bài toán

Trong các trò chơi đối kháng hai người (ví dụ: **Cờ caro, Tic-Tac-Toe, Cờ vua**), mỗi người chơi đều cố gắng **tối ưu hóa lợi ích của mình** và **giảm lợi ích của đối thủ**.

Thuật toán **Minimax** được sử dụng để tìm **nước đi tối ưu nhất**, giả sử rằng:
- Người chơi **MAX** luôn chọn nước đi có lợi nhất cho mình
- Người chơi **MIN** luôn chọn nước đi bất lợi nhất cho MAX

---

## 🔷 9. Nguyên lý thuật toán Minimax

Thuật toán Minimax xây dựng **cây trò chơi** với các mức (depth):

- 🌟 **MAX level**: chọn giá trị **lớn nhất**
- 🔻 **MIN level**: chọn giá trị **nhỏ nhất**

Giá trị của một trạng thái được xác định dựa trên:
- Trạng thái **kết thúc** (thắng / thua / hòa)
- Hoặc **hàm đánh giá (heuristic)** nếu chưa kết thúc

---

## 🔷 10. Hàm đánh giá (Evaluation Function)

Trong bài toán cờ caro, hàm đánh giá có thể được xây dựng dựa trên:
- Số chuỗi liên tiếp của MAX
- Số chuỗi liên tiếp của MIN
- Trạng thái thắng / thua

Ví dụ:
- MAX thắng → điểm = +10
- MIN thắng → điểm = −10
- Hòa → điểm = 0

---

## 🔷 11. Mã giả thuật toán Minimax

```text
function MINIMAX(state, depth, isMax):
    nếu state là trạng thái kết thúc hoặc depth = 0:
        return giá trị đánh giá(state)

    nếu isMax:
        best = −∞
        cho mỗi nước đi hợp lệ:
            best = max(best, MINIMAX(state mới, depth−1, false))
        return best
    ngược lại:
        best = +∞
        cho mỗi nước đi hợp lệ:
            best = min(best, MINIMAX(state mới, depth−1, true))
        return best

```
---

# 🎨 THUẬT TOÁN TÔ MÀU ĐỒ THỊ (GRAPH COLORING)

## 🔷 19. Giới thiệu

**Bài toán tô màu đồ thị** (*Graph Coloring Problem*) là một bài toán cơ bản trong **Trí tuệ nhân tạo** và **Lý thuyết đồ thị**.

Mục tiêu của bài toán là:
> **Gán màu cho các đỉnh của đồ thị sao cho không có hai đỉnh kề nhau cùng màu**, đồng thời **số màu sử dụng là ít nhất**.

---

## 🔷 20. Mô tả bài toán

Cho:
- Một đồ thị \( G = (V, E) \)
- Tập đỉnh \( V \)
- Tập cạnh \( E \)

Yêu cầu:
- Mỗi đỉnh \( v \in V \) được gán **một màu**
- Với mọi cạnh \( (u, v) \in E \):  
  \[
  color(u) \neq color(v)
  \]

---

## 🔷 21. Ứng dụng của tô màu đồ thị

Bài toán tô màu đồ thị được ứng dụng rộng rãi trong thực tế:

- 📅 Lập lịch thi / thời khóa biểu
- 📡 Phân bổ tần số vô tuyến
- 🧠 Giải bài toán ràng buộc (CSP)
- 🗺️ Bản đồ – tô màu các vùng sao cho không trùng nhau

---

## 🔷 22. Độ khó của bài toán

- Bài toán tô màu đồ thị là **NP-Hard**
- Việc tìm **số màu tối thiểu** là bài toán khó
- Trong thực tế thường dùng **thuật toán xấp xỉ (heuristic)**

---

## 🔷 23. Thuật toán Greedy Graph Coloring

### 🔹 23.1. Ý tưởng

Thuật toán **Greedy Coloring** tô màu các đỉnh theo thứ tự:
- Với mỗi đỉnh, chọn **màu nhỏ nhất** chưa bị dùng bởi các đỉnh kề

Thuật toán **nhanh**, dễ cài đặt nhưng **không đảm bảo tối ưu**.

---

### 🔹 23.2. Các bước thực hiện

1. Sắp xếp các đỉnh theo một thứ tự (thường theo **bậc giảm dần**)
2. Gán màu cho đỉnh đầu tiên
3. Với mỗi đỉnh tiếp theo:
   - Xác định các màu đã bị dùng bởi đỉnh kề
   - Chọn màu nhỏ nhất chưa bị sử dụng

---

## 🔷 24. Mã giả thuật toán Greedy Coloring

```text
Sắp xếp các đỉnh theo bậc giảm dần
color(v) ← −1 với mọi v

for mỗi đỉnh v theo thứ tự:
    used_colors ← các màu của đỉnh kề v
    chọn màu nhỏ nhất không thuộc used_colors
    gán màu đó cho v
