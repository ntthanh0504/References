# Dữ liệu lớn (Big Data) & Khai thác dữ liệu (Data Mining)

### 1. Big Data đang thúc đẩy chuyển đổi số như thế nào?
Chuyển đổi số không đơn giản chỉ là việc sao chép các quy trình hiện có dưới dạng kỹ thuật số; việc phân tích chuyên sâu về cách thức vận hành của doanh nghiệp giúp các tổ chức khám phá ra cách cải thiện quy trình và hoạt động của họ, đồng thời khai thác lợi ích từ việc tích hợp khoa học dữ liệu vào quy trình làm việc. 

Hầu hết các tổ chức đều nhận ra rằng việc chuyển đổi số sẽ đòi hỏi những thay đổi căn bản về cách tiếp cận của họ đối với dữ liệu, nhân viên và khách hàng, đồng thời sẽ ảnh hưởng đến văn hóa tổ chức. 

Đây là một sự thay đổi về tổ chức và văn hóa được thúc đẩy bởi `Big Data`.


### 2. Giới thiệu về Đám Mây (Cloud)
Điện toán đám mây là việc cung cấp các tài nguyên điện toán theo yeeui cầu thông qua Internet the mô hình trả tiền theo mức sử dụng.

- **5 đặc điểm thiết yếu:**
  - Tự phục vụ theo yêu cầu (on-demand self-service): có thể truy cập vào các tài nguyên đám mây bằng cách sử dụng một giao diện đơn giản, mà không cần tương tác với con người tại mỗi nhà cung cấp dịch vụ.

  - Truy cập mạng rộng rãi (broad network access): các tài nguyên có thể được truy cập thông qua mạng.

  - Gộp tài nguyên (resource pooling): Sử dụng mô hình đa khách hàng (multitenant model), các tài nguyên điện toán được tổng hợp để phục vụ nhiều người tiêu dùng. Các tài nguyên đám mây được gán và gán lại một cách linh hoạt theo nhu cầu, mà khách hàng không cần biết vị trí vật lý của các tài nguyên này.

  - Tính đàn hồi nhanh chóng (rapid elasticity): truy cập nhiều tài nguyên khi cần và giảm quy mô khi không cần.

  - Dịch vụ được đo lường (measured service): chỉ trả tiền cho những gì bạn sử dụng hoặc dự phòng trước khi sử dụng.

- **3 mô hình triển khai:**
  - Public: tân dụng các dịch vụ mở trên phần cứng thuộc sở hữu của nhà cung cấp đám mây, nhưng việc sử dụng nó được chia sẻ bởi các công ty khác.

  - Private: cơ sở hạ tầng đám mây được cung cấp để sử dụng độc quyền bởi một tổ chức duy nhất.

  - Hybrid: là sự kết hợp của 2 mô hình trên, hoạt động cùng nhau một cách liền mạch.

- **3 mô hình dịch vụ đám mây** dựa trên ba lớp trong một ngăn xếp điện toán (cơ sở hạ tầng, nền tảng và ứng dụng):
  - Infrastructure as a Service (IaaS): truy cập vào cơ sở hạ tầng và các tài nguyên điện toán vật lý.

  - Platform as a Service (PaaS): truy cập các công cụ phần cứng và phần mềm cần thiết để phát triển và triển khai các ứng dụng cho người dùng.

  - Software as a Service (SaaS): mô hình cấp phép và phân phối phần mềm. Đôi khi nó được gọi là 'phần mềm theo yêu cầu'.

### 3. Đám mây cho Khoa học dữ liệu
Sử dụng Điện toán Đám mây cho phép bạn truy cập tức thời vào các công nghệ nguồn mở như Apache Spark mà không cần cài đặt và cấu hình cục bộ.

Điện toán Đám mây cũng cung cấp cho bạn quyền truy cập vào các công cụ và thư viện mới nhất mà không cần lo lắng về việc bảo trì và đảm bảo chúng được cập nhật.

Điện toán Đám mây có thể truy cập từ mọi nơi và mọi múi giờ. Nhiều nhà cộng tác hoặc nhóm có thể truy cập dữ liệu đồng thời, cùng nhau hợp tác để đưa ra giải pháp.

Một số công ty công nghệ lớn cung cấp nền tảng Đám mây, cho phép bạn làm quen với các công nghệ đám mây trong môi trường được xây dựng sẵn. 
- IBM cung cấp IBM Cloud

- Amazon cung cấp Amazon Web Services (AWS) 

- Google cung cấp Google Cloud Platform.

### 4. Định nghĩa của Dữ liệu lớn
Big Data không có một định nghĩa duy nhất, nhưng có một số yếu tố chung, được gọi là "V" cơ bản của Big Data:

- **Vận tốc (Velocity):** Tốc độ tích lũy dữ liệu, được tạo ra liên tục và không ngừng. Công nghệ truyền phát trực tuyến thời gian thực có khả năng xử lý thông tin nhanh chóng.

- **Khối lượng (Volume):** Quy mô của dữ liệu, với sự gia tăng không ngừng của lượng dữ liệu được lưu trữ. Yếu tố này thúc đẩy bởi sự gia tăng nguồn dữ liệu và cơ sở hạ tầng mở rộng.

- **Sự đa dạng (Variety):** Tính đa dạng của dữ liệu, bao gồm cả dữ liệu có cấu trúc và phi cấu trúc, đến từ nhiều nguồn khác nhau như máy móc, con người và quy trình tổ chức.

- **Độ chính xác (Veracity):** Chất lượng và nguồn gốc của dữ liệu, cũng như tính chính xác và phù hợp của nó với thực tế. Thuộc tính này bao gồm tính nhất quán, đầy đủ và toàn vẹn.

- **Giá trị (Value):** Khả năng chuyển đổi dữ liệu thành giá trị, không chỉ là lợi nhuận mà còn là lợi ích xã hội, hài lòng của khách hàng hoặc cá nhân.

### 5. Công cụ xử lý Dữ liệu lớn

**Hadoop** là một nền tảng mã nguồn mở dựa trên Java, cho phép lưu trữ và xử lý dữ liệu lớn trên các cụm máy tính phân tán. Hadoop có thể mở rộng linh hoạt từ một nút đến nhiều nút và cung cấp lưu trữ đáng tin cậy và tiết kiệm chi phí. 

Bằng cách sử dụng Hadoop, bạn có thể: 
- Kết hợp nhiều loại dữ liệu khác nhau từ các nguồn mới.

- Cung cấp quyền truy cập tự phục vụ theo thời gian thực.

- Tối ưu hóa việc lưu trữ và di chuyển dữ liệu không thường xuyên sử dụng sang hệ thống Hadoop để tiết kiệm chi phí.

**HDFS**, hay Hadoop Distributed File System, là một thành phần quan trọng của Hadoop, dùng để lưu trữ dữ liệu lớn trên nhiều máy tính thông dụng kết nối qua mạng. Nó phân chia dữ liệu thành nhiều phần và lưu trữ chúng trên các nút khác nhau, cho phép truy cập song song và sao chép để đảm bảo tính sẵn có và độ tin cậy cao. 

HDFS cung cấp nhiều lợi ích, bao gồm:
- Mở rộng dễ dàng: HDFS cho phép chia nhỏ công việc và chạy chúng song song trên nhiều máy tính, cải thiện khả năng mở rộng của hệ thống.

- Tối ưu hóa hiệu suất: Nó giảm thiểu nghẽn mạng và tăng thông lượng bằng cách di chuyển tính toán gần hơn tới nút lưu trữ dữ liệu.

- Khôi phục nhanh chóng: HDFS có khả năng phát hiện và phục hồi tự động sau sự cố phần cứng.

- Truy cập dữ liệu streaming: Hỗ trợ tốc độ truyền dữ liệu cao.

- Khả năng chứa dữ liệu lớn: HDFS có thể mở rộng linh hoạt ra hàng trăm nút hoặc máy tính trong một cụm.

- Tính di động: Có thể di chuyển trên nhiều nền tảng phần cứng và tương thích với nhiều hệ điều hành khác nhau.

**Hive** là một phần mềm kho dữ liệu mã nguồn mở cho việc quản lý và truy cập các tập dữ liệu lớn trong HDFS hoặc các hệ thống lưu trữ khác. Tuy nhiên, do đặc điểm của Hadoop, Hive thích hợp cho các công việc như ETL, báo cáo và phân tích dữ liệu, nhưng không phù hợp cho xử lý giao dịch.

**Spark** là một công cụ đa dụng cho xử lý dữ liệu lớn, có thể thực hiện nhiều ứng dụng khác nhau như Phân tích Tương tác, Xử lý Dữ liệu Luồng, Máy Học và ETL. Spark tận dụng khả năng xử lý trong bộ nhớ để tăng tốc độ tính toán và có khả năng truy cập dữ liệu từ nhiều nguồn khác nhau, bao gồm HDFS và Hive, giúp nó trở nên rất linh hoạt.

Với khả năng xử lý dữ liệu nhanh chóng và thực hiện phân tích phức tạp trong thời gian thực, Apache Spark được sử dụng chủ yếu cho các ứng dụng cần phản hồi nhanh và yêu cầu hiệu suất cao.

<div style="font-size:15px; font-family: Arial, sans-serif; ">

### 6. Quy trình khai thác dữ liệu (Data Mining)

1. Xác định mục tiêu
   - Xác định các câu hỏi chính cần trả lời

   - Cân nhắc chi phí và lợi ích của quá trình khai thác dữ liệu

   - Mức độ chính xác mong đợi từ kết quả cũng ảnh hưởng đến chi phí: Độ chính xác cao hơn sẽ tốn nhiều chi phí hơn và ngược lại. 

2. Lựa chọn dữ liệu:
   - Kết quả của quá trình khai thác dữ liệu phụ thuộc rất nhiều vào chất lượng của dữ liệu được sử dụng. 

   - Xác định đúng loại dữ liệu cần thiết cho quy trình khai thác - loại dữ liệu có thể trả lời các câu hỏi đặt ra với chi phí hợp lý - là rất quan trọng.

3. Tiền xử lý dữ liệu:
   - Xác định và loại bỏ các thuộc tính không liên quan: Phân biệt và loại bỏ những thông tin không cần thiết cho phân tích.

   - Xác định và xử lý lỗi: Kiểm tra và sửa các lỗi do con người gây ra để đảm bảo tính toàn vẹn của dữ liệu.

   - Xử lý dữ liệu bị thiếu: Đối phó với dữ liệu bị thiếu bằng cách xác định nguyên nhân và áp dụng phương pháp xử lý phù hợp.

4. Chuyển đổi dữ liệu
    - Xác định định dạng lưu trữ dữ liệu phù hợp.

    - Giảm thiểu số lượng thuộc tính cần thiết để giải thích hiện tượng. 
    
    - Chuyển đổi các biến để giúp giải thích hiện tượng đang được nghiên cứu. 
    
    - Chuyển đổi biến từ loại này sang loại khác.

5. Lưu trữ dữ liệu: 
   - Dữ liệu đã được chuyển đổi phải được lưu trữ ở định dạng phù hợp.

   - An toàn và bảo mật dữ liệu là mối quan tâm hàng đầu khi lưu trữ dữ liệu.

6. Khai thác dữ liệu
   -  Các phương pháp phân tích dữ liệu, bao gồm các phương pháp tham số và phi tham số, và các thuật toán học máy.

   - Khởi đầu hiệu quả cho khai thác dữ liệu là trực quan hóa dữ liệu - hữu ích trong việc xây dựng hiểu biết sơ bộ về các xu hướng ẩn trong tập dữ liệu.

7. Đánh giá kết quả
   - Đánh giá chính thức có thể bao gồm việc kiểm tra khả năng dự đoán của các mô hình trên dữ liệu quan sát để xem các thuật toán hiệu quả và chính xác như thế nào trong việc tái tạo dữ liệu. Điều này được gọi là "dự báo trong mẫu" (in-sample forecast).

   - Ngoài ra, kết quả được chia sẻ với các bên liên quan chính để lấy ý kiến phản hồi, sau đó được kết hợp vào các lần lặp lại khai thác dữ liệu sau để cải thiện quá trình.

   - Khai thác dữ liệu và đánh giá kết quả trở thành một quá trình lặp.
 
# Học sâu (Deep Learning) & Học máy (Machine Learning) 

### 1. Trí tuệ nhân tạo
Học máy là yếu tố cho phép máy móc tự giải quyết vấn đề và đưa ra các dự đoán chính xác bằng cách sử dụng dữ liệu được cung cấp.

Học sâu sử dụng mạng nơ-ron nhiều lớp để mô phỏng quá trình ra quyết định của con người - cho phép AI học hỏi liên tục, cải thiện chất lượng và độ chính xác.

Mạng nơ rơn là tập hợp các đơn vị tính toán nhỏ gọi là nơ-ron, có khả năng tiếp nhận dữ liệu đầu vào và học cách đưa ra quyết định theo thời gian.

> Mạng nơ-ron thường có nhiều lớp - Học sâu trở nên hiệu quả khi lượng dữ liệu tăng lên trái ngược với các thuật toán học máy có thể đạt đến giới hạn khi dữ liệu tăng.

### 2. Trí tuệ nhân tạo tạo sinh
Tập trung vào việc tạo dữ liệu mới thay vì chỉ phân tích dữ liệu hiện có. Nó cho phép máy móc tạo nội dung bao gồm hình ảnh, âm nhạc, ngôn ngữ, mã máy tính, ...

Generative Adversarial Networks (GANs) and Variational Autoencoders (VAEs) là nền tảng của kỹ thuật này. Chúng tạo ra các phiên bản mới sao chép phân bố cơ bản của dữ liệu ban đầu bằng cách học các mẫu từ lượng lớn dữ liệu.

Các nhà khoa học dữ liệu, nhà nghiên cứu và nhà phân tích thường xuyên gặp phải hạn chế về thời gian khi nghiên cứu các mẫu dữ liệu và rút ra các thông tin chi tiết. Do hạn chế này, họ chỉ có thể xây dựng, phát triển và đánh giá một số lượng nhỏ các giả thuyết, bỏ mặc nhiều khả năng khác chưa được kiểm tra. Với generative AI, các nhà khoa học dữ liệu có thể tận dụng kỹ thuật này để tạo và kiểm tra mã phần mềm, phục vụ cho việc xây dựng các mô hình phân tích.

### 3. Mạng nơ-ron và học sâu
Chúng ta có các mạng nơ-ron và học sâu, chúng có thể nhận dạng giọng nói, nhận dạng người, biết bạn đã đến đó, nhận dạng khuôn mặt của bạn.

Rất nhiều thứ trong lĩnh vực này dựa trên ma trận và đại số tuyến tính. Vì vậy, bạn cần biết cách sử dụng đại số tuyến tính để thực hiện các phép biến đổi. 

Tuy nhiên, hiện nay có rất nhiều gói công cụ giúp thực hiện học sâu và chúng sẽ xử lý tất cả các phép tính đại số tuyến tính cho bạn, nhưng bạn vẫn nên hiểu được những gì đang diễn ra bên dưới. 

Học sâu đặc biệt cần sức mạnh tính toán rất cao.