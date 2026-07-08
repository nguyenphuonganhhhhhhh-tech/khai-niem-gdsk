import streamlit as st

# Thiết lập cấu hình trang hiển thị trực quan
st.set_page_config(page_title="Trắc nghiệm TT-GDSK", page_icon="📢", layout="centered")

# --- DỮ LIỆU 50 CÂU HỎI TRẮC NGHIỆM ---
quiz_data = [
    # PHẦN I — MỨC ĐỘ DỄ (Câu 1–15)
    {"q": "Câu 1. Thông tin là gì?", "ops": ["A. Quá trình chuyển đi các tin tức, sự kiện từ một nguồn phát tới đối tượng nhận tin", "B. Hoạt động cung cấp thông tin, thông điệp được lặp đi lặp lại nhiều lần theo một chiều", "C. Tác động có hệ thống đến sự phát triển tinh thần, thể chất của con người", "D. Quá trình tác động liên tục có mục đích, kế hoạch đến suy nghĩ và tình cảm con người"], "ans": "A"},
    {"q": "Câu 2. Tuyên truyền có đặc điểm gì về chiều truyền tin?", "ops": ["A. Hai chiều", "B. Một chiều", "C. Đa chiều", "D. Không có chiều nhất định"], "ans": "B"},
    {"q": "Câu 3. Theo bài học, giáo dục được định nghĩa là gì?", "ops": ["A. Tác động có hệ thống đến sự phát triển tinh thần, thể chất của con người để họ có phẩm chất, năng lực theo yêu cầu", "B. Quá trình chuyển tin tức từ nguồn phát tới đối tượng nhận", "C. Hoạt động cung cấp thông tin lặp lại nhiều lần", "D. Số đo giúp đo lường và so sánh sự thay đổi"], "ans": "A"},
    {"q": "Câu 4. Truyền thông – Giáo dục sức khỏe (TT-GDSK) nhằm mục đích gì?", "ops": ["A. Chỉ nâng cao kiến thức của đối tượng", "B. Chỉ thay đổi thái độ của đối tượng", "C. Nâng cao kiến thức, thay đổi thái độ và thay đổi hành vi/thực hành về sức khỏe", "D. Chỉ thay đổi hành vi mà không cần kiến thức, thái độ"], "ans": "C"},
    {"q": "Câu 5. Tuyên ngôn Ottawa về nâng cao sức khỏe được thông qua vào năm nào?", "ops": ["A. 1978", "B. 1986", "C. 1990", "D. 2000"], "ans": "B"},
    {"q": "Câu 6. Tuyên ngôn Ottawa được thông qua tại quốc gia nào?", "ops": ["A. Hoa Kỳ", "B. Anh", "C. Canada", "D. Thụy Sĩ"], "ans": "C"},
    {"q": "Câu 7. Chỉ số y tế/sức khỏe được định nghĩa là gì?", "ops": ["A. Thước đo giá trị các mục tiêu, kết quả và hoạt động y tế xã hội", "B. Số đo giúp đo lường và so sánh những sự thay đổi", "C. Quá trình chuyển tin tức từ nguồn phát tới đối tượng nhận", "D. Hoạt động cung cấp thông tin lặp đi lặp lại"], "ans": "B"},
    {"q": "Câu 8. Chỉ tiêu y tế/sức khỏe được định nghĩa là gì?", "ops": ["A. Số đo giúp đo lường và so sánh sự thay đổi", "B. Thước đo giá trị các mục tiêu, kết quả và hoạt động y tế xã hội", "C. Quá trình học tập liên tục", "D. Chuỗi các hành động lặp đi lặp lại"], "ans": "B"},
    {"q": "Câu 9. Hành vi được định nghĩa là gì?", "ops": ["A. Một chuỗi các hành động lặp đi lặp lại", "B. Một hoạt động đơn lẻ, ngẫu nhiên không có mục đích", "C. Quá trình học tập liên tục", "D. Sự tác động có hệ thống đến tinh thần con người"], "ans": "A"},
    {"q": "Câu 10. Theo bài học, có bao nhiêu nguyên tắc chính trong TT-GDSK?", "ops": ["A. 4", "B. 5", "C. 6", "D. 7"], "ans": "C"},
    {"q": "Câu 11. Đâu KHÔNG phải là một trong các nguyên tắc TT-GDSK đã học?", "ops": ["A. Nguyên tắc khoa học", "B. Nguyên tắc đại chúng", "C. Nguyên tắc trực quan", "D. Nguyên tắc cạnh tranh"], "ans": "D"},
    {"q": "Câu 12. Nguyên tắc đại chúng trong TT-GDSK nhấn mạnh điều gì?", "ops": ["A. Chỉ tác động vào giác quan của đối tượng", "B. Mọi người cùng tham gia, cùng thực hiện, xuất phát từ nhu cầu cộng đồng", "C. Chỉ dựa trên cơ sở y học đơn thuần", "D. Chỉ áp dụng ở tuyến trung ương"], "ans": "B"},
    {"q": "Câu 13. Nguyên tắc trực quan trong TT-GDSK chủ yếu tác động vào đâu?", "ops": ["A. Nhận thức lý tính", "B. Các giác quan (mắt, tai, mũi...)", "C. Hệ thống chính sách y tế", "D. Cơ cấu tổ chức ngành y tế"], "ans": "B"},
    {"q": "Câu 14. Nguyên tắc thực tiễn trong TT-GDSK yêu cầu điều gì?", "ops": ["A. Phải bắt nguồn từ các vấn đề sức khỏe thực tế của cộng đồng", "B. Chỉ dựa vào lý thuyết sách vở", "C. Không cần sự tham gia của cộng đồng", "D. Chỉ áp dụng riêng cho cán bộ y tế"], "ans": "A"},
    {"q": "Câu 15. Nguyên tắc lồng ghép trong TT-GDSK có nghĩa là gì?", "ops": ["A. Chỉ thực hiện độc lập, không phối hợp với ngành khác", "B. Kết hợp TT-GDSK với hoạt động của các ngành khác như giáo dục, thông tin - truyền thông", "C. Chỉ áp dụng tại tuyến xã, phường", "D. Không cần đưa vào các chương trình khác"], "ans": "B"},

    # PHẦN II — MỨC ĐỘ TRUNG BÌNH (Câu 16–35)
    {"q": "Câu 16. Thông tin y tế có mấy nghĩa theo bài học?", "ops": ["A. 1", "B. 2", "C. 3", "D. 4"], "ans": "B"},
    {"q": "Câu 17. Theo nghĩa thứ nhất, thông tin y tế được hiểu là gì?", "ops": ["A. Truyền tin/thông điệp về sức khỏe", "B. Tin tức, số liệu, chỉ tiêu về sức khỏe", "C. Thước đo giá trị mục tiêu y tế", "D. Chuỗi hành động lặp đi lặp lại"], "ans": "A"},
    {"q": "Câu 18. Theo nghĩa thứ hai, thông tin y tế được hiểu là gì?", "ops": ["A. Chỉ là hoạt động truyền tin về sức khỏe", "B. Tin tức/thông điệp, số liệu, chỉ tiêu/chỉ số về sức khỏe", "C. Hoạt động chính trị ảnh hưởng đến sức khỏe", "D. Quá trình học tập liên tục"], "ans": "B"},
    {"q": "Câu 19. Theo Tuyên ngôn Ottawa, nâng cao sức khỏe gồm mấy nội dung/hoạt động chính?", "ops": ["A. 3", "B. 4", "C. 5", "D. 6"], "ans": "C"},
    {"q": "Câu 20. Đâu KHÔNG thuộc 5 nội dung nâng cao sức khỏe theo Tuyên ngôn Ottawa?", "ops": ["A. Xây dựng chính sách công cộng lành mạnh", "B. Tạo ra môi trường hỗ trợ", "C. Nâng cao hành động của cộng đồng", "D. Tăng cường quảng cáo thương mại"], "ans": "D"},
    {"q": "Câu 21. Nội dung 'Tạo ra môi trường hỗ trợ' trong nâng cao sức khỏe chú trọng điều gì?", "ops": ["A. Điều kiện sống, làm việc an toàn và bảo vệ môi trường tự nhiên", "B. Đào tạo cán bộ y tế", "C. Ban hành luật pháp, thuế quan", "D. Phát triển kỹ năng cá nhân"], "ans": "A"},
    {"q": "Câu 22. Nội dung 'Phát triển kỹ năng của con người' được thực hiện chủ yếu ở đâu?", "ops": ["A. Chỉ tại bệnh viện", "B. Trường học, gia đình, nơi làm việc và cộng đồng", "C. Chỉ tại cơ quan nhà nước", "D. Chỉ tại trung tâm y tế dự phòng"], "ans": "B"},
    {"q": "Câu 23. Nội dung 'Định hướng lại dịch vụ chăm sóc sức khỏe' nhấn mạnh điều gì?", "ops": ["A. Hệ thống y tế cần đóng góp vào sự nghiệp nâng cao sức khỏe và đào tạo cán bộ y tế", "B. Chỉ tập trung điều trị bệnh", "C. Không cần lồng ghép với chính sách sức khỏe", "D. Bỏ qua nhu cầu nâng cao sức khỏe của người dân"], "ans": "A"},
    {"q": "Câu 24. 'Hỗ trợ truyền thông' (advocacy communication) gồm những hoạt động nào?", "ops": ["A. Chỉ hoạt động quảng cáo thương mại", "B. Thông tin, hoạt động giáo dục và các hoạt động thúc đẩy nhằm động viên sự tham gia", "C. Chỉ tuyên truyền một chiều", "D. Chỉ đào tạo cán bộ y tế"], "ans": "B"},
    {"q": "Câu 25. ' Tiếp thị xã hội' (social marketing) trong TT-GDSK là gì?", "ops": ["A. Vận dụng tiếp thị thương mại và các giải pháp quảng cáo cho vấn đề sức khỏe", "B. Chỉ áp dụng các quy định pháp luật", "C. Hoạt động riêng của tuyến xã, phường", "D. Một nguyên tắc khoa học của TT-GDSK"], "ans": "A"},
    {"q": "Câu 26. Vai trò của TT-GDSK trong chăm sóc sức khỏe thể hiện đầy đủ nhất ở điều nào?", "ops": ["A. Chỉ giúp người bệnh hiểu chỉ định điều trị", "B. Giúp hiểu biết vấn đề sức khỏe, quyết định hành động thích hợp và thực hiện đúng chỉ định điều trị", "C. Chỉ có vai trò tuyên truyền pháp luật", "D. Không có vai trò trong chăm sóc sức khỏe cộng đồng"], "ans": "B"},
    {"q": "Câu 27. Cơ quan nào là cơ quan chuyên môn cao nhất, chỉ đạo hoạt động TT-GDSK ở tuyến trung ương?", "ops": ["A. Trung tâm TT-GDSK Bộ Y tế", "B. Sở Y tế tỉnh", "C. Trạm y tế xã/phường", "D. Bệnh viện trung ương"], "ans": "A"},
    {"q": "Câu 28. Ở tuyến tỉnh, cơ quan nào chịu trách nhiệm chỉ đạo hoạt động TT-GDSK?", "ops": ["A. Trung tâm TT-GDSK trực thuộc Sở Y tế tỉnh/thành phố", "B. UBND tỉnh", "C. Bộ Y tế", "D. Trường Đại học Y"], "ans": "A"},
    {"q": "Câu 29. Ở tuyến xã, phường, ai chịu trách nhiệm về mọi hoạt động TT-GDSK?", "ops": ["A. Chủ tịch UBND xã", "B. Trưởng trạm y tế xã/phường", "C. Giám đốc Sở Y tế", "D. Trưởng thôn"], "ans": "B"},
    {"q": "Câu 30. Cơ sở khoa học nào của TT-GDSK liên quan đến 'cách ứng xử của con người và vì sao con người lại ứng xử như vậy'?", "ops": ["A. Cơ sở khoa học y học", "B. Cơ sở khoa học hành vi", "C. Cơ sở tâm lý học giáo dục", "D. Cơ sở tâm lý học nhận thức"], "ans": "B"},
    {"q": "Câu 31. Theo tháp nhu cầu Maslow, nhu cầu nào là cơ bản/thấp nhất?", "ops": ["A. Nhu cầu tự khẳng định", "B. Nhu cầu được tôn trọng", "C. Nhu cầu xã hội", "D. Nhu cầu sinh lý"], "ans": "D"},
    {"q": "Câu 32. Theo tháp nhu cầu Maslow, nhu cầu nào ở bậc cao nhất?", "ops": ["A. Nhu cầu sinh lý", "B. Nhu cầu an toàn", "C. Nhu cầu tự khẳng định", "D. Nhu cầu xã hội"], "ans": "C"},
    {"q": "Câu 33. Sắp xếp đúng thứ tự tháp nhu cầu Maslow từ thấp đến cao:", "ops": ["A. Sinh lý \u2192 An toàn \u2192 Xã hội \u2192 Tôn trọng \u2192 Tự khẳng định", "B. An toàn \u2192 Sinh lý \u2192 Tôn trọng \u2192 Xã hội \u2192 Tự khẳng định", "C. Tự khẳng định \u2192 Tôn trọng \u2192 Xã hội \u2192 An toàn \u2192 Sinh lý", "D. Xã hội \u2192 Sinh lý \u2192 An toàn \u2192 Tự khẳng định \u2192 Tôn trọng"], "ans": "A"},
    {"q": "Câu 34. Lý thuyết phổ biến sự đổi mới mô tả quá trình chấp nhận cái mới theo trình tự nào?", "ops": ["A. Khởi xướng \u2192 chấp nhận \u2192 đa số sớm \u2192 đa số muộn \u2192 lạc hậu, bảo thủ", "B. Đa số sớm \u2192 khởi xướng \u2192 đa số muộn \u2192 lạc hậu", "C. Lạc hậu \u2192 bảo thủ \u2192 chấp nhận \u2192 khởi xướng", "D. Chấp nhận \u2192 khởi xướng \u2192 lạc hậu \u2192 đa số muộn"], "ans": "A"},
    {"q": "Câu 35. Cơ sở tâm lý học nhận thức trong TT-GDSK bao gồm những loại nhận thức nào?", "ops": ["A. Nhận thức cảm tính và nhận thức lý tính", "B. Nhận thức chủ động và nhận thức bị động", "C. Nhận thức xã hội và nhận thức cá nhân", "D. Nhận thức khoa học và nhận thức thực tiễn"], "ans": "A"},

    # PHẦN III — MỨC ĐỘ KHÓ (Câu 36–50)
    {"q": "Câu 36. Điểm khác biệt cơ bản nhất giữa 'thông tin' và 'tuyên truyền' là gì?", "ops": ["A. Thông tin chỉ tồn tại dưới dạng số liệu, tuyên truyền thì không", "B. Thông tin là chuyển tin tức từ nguồn phát tới đối tượng nhận (có thể đa chiều), tuyên truyền là cung cấp thông tin lặp đi lặp lại theo một chiều", "C. Không có sự khác biệt giữa hai khái niệm", "D. Tuyên truyền chỉ dùng trong y tế, thông tin dùng trong mọi lĩnh vực"], "ans": "B"},
    {"q": "Câu 37. Vì sao 'thay đổi hành vi' trong TT-GDSK được xem là khó khăn, đòi hỏi nguyên tắc khoa học?", "ops": ["A. Vì hành vi hình thành từ nhiều yếu tố (nhận thức, tâm lý, xã hội) nên cần cơ sở khoa học đa chiều để tác động hiệu quả", "B. Vì hành vi không thể thay đổi được", "C. Vì hành vi chỉ phụ thuộc vào ý muốn cá nhân, không cần cơ sở khoa học", "D. Vì hành vi không liên quan đến sức khỏe"], "ans": "A"},
    {"q": "Câu 38. Một chương trình chỉ phát áp phích, tờ rơi mà không có sự tham gia/phản hồi hai chiều của cộng đồng thì thiên về:", "ops": ["A. Giáo dục", "B. Tuyên truyền", "C. Nâng cao sức khỏe", "D. Vận động xã hội"], "ans": "B"},
    {"q": "Câu 39. Một cán bộ y tế tổ chức TT-GDSK bằng tiếng dân tộc địa phương và huy động chính quyền, đoàn thể cùng tham gia. Cán bộ đó đang áp dụng chủ yếu nguyên tắc nào?", "ops": ["A. Nguyên tắc khoa học", "B. Nguyên tắc đại chúng", "C. Nguyên tắc trực quan", "D. Nguyên tắc lồng ghép"], "ans": "B"},
    {"q": "Câu 40. Một chương trình sử dụng quá nhiều tranh ảnh, mô hình cho cả những nội dung đơn giản là biểu hiện của việc vi phạm điều gì trong nguyên tắc trực quan?", "ops": ["A. Thiếu tính khoa học", "B. Lạm dụng phương tiện trực quan không cần thiết", "C. Thiếu tính đại chúng", "D. Thiếu tính thực tiễn"], "ans": "B"},
    {"q": "Câu 41. Việc lồng ghép nội dung TT-GDSK vào chương trình giảng dạy của ngành giáo dục thể hiện nguyên tắc nào?", "ops": ["A. Nguyên tắc lồng ghép", "B. Nguyên tắc trực quan", "C. Nguyên tắc đại chúng", "D. Nguyên tắc khoa học"], "ans": "A"},
    {"q": "Câu 42. Việc xây dựng chính sách thuế đối với thuốc lá nhằm hạn chế hút thuốc thuộc nội dung nào trong 5 nội dung nâng cao sức khỏe của Ottawa?", "ops": ["A. Tạo ra môi trường hỗ trợ", "B. Xây dựng chính sách công cộng lành mạnh", "C. Phát triển kỹ năng cá nhân", "D. Định hướng lại dịch vụ y tế"], "ans": "B"},
    {"q": "Câu 43. Việc tổ chức tập huấn kỹ năng phòng chống bệnh mạn tính cho người dân tại trường học, nơi làm việc thuộc nội dung nào?", "ops": ["A. Nâng cao hành động cộng đồng", "B. Phát triển kỹ năng của con người", "C. Tạo môi trường hỗ trợ", "D. Định hướng dịch vụ y tế"], "ans": "B"},
    {"q": "Câu 44. Cộng đồng tự tổ chức, huy động nguồn lực để giải quyết vấn đề vệ sinh môi trường của chính mình là ví dụ của nội dung nào trong nâng cao sức khỏe?", "ops": ["A. Xây dựng chính sách công cộng", "B. Nâng cao hành động của cộng đồng", "C. Định hướng dịch vụ chăm sóc sức khỏe", "D. Nguyên tắc khoa học"], "ans": "B"},
    {"q": "Câu 45. Việc Trung tâm TT-GDSK Bộ Y tế đảm nhận đào tạo, đào tạo lại nghiệp vụ cho cán bộ tất cả các tuyến phản ánh vai trò gì?", "ops": ["A. Vai trò định hướng, chỉ đạo và nâng cao năng lực cho toàn hệ thống", "B. Vai trò chỉ thực hiện tại chỗ, không liên quan tuyến dưới", "C. Vai trò chỉ nghiên cứu khoa học đơn thuần", "D. Vai trò chỉ quản lý tài chính"], "ans": "A"},
    {"q": "Câu 46. Sự khác biệt cốt lõi giữa 'nguyên tắc khoa học' và 'nguyên tắc thực tiễn' trong TT-GDSK là gì?", "ops": ["A. Nguyên tắc khoa học dựa trên cơ sở lý luận y học/tâm lý/xã hội; nguyên tắc thực tiễn đòi hỏi xuất phát và giải quyết vấn đề sức khỏe cụ thể của cộng đồng", "B. Hai nguyên tắc này hoàn toàn giống nhau", "C. Nguyên tắc thực tiễn không cần dựa trên cơ sở khoa học", "D. Nguyên tắc khoa học không thể áp dụng vào thực tế"], "ans": "A"},
    {"q": "Câu 47. Vì sao TT-GDSK và nâng cao sức khỏe có mối quan hệ chặt chẽ nhưng không đồng nhất?", "ops": ["A. Vì TT-GDSK là một trong những phương thức để đạt mục tiêu nâng cao sức khỏe, trong khi nâng cao sức khỏe bao hàm nhiều hoạt động rộng hơn như chính sách, môi trường", "B. Vì hai khái niệm hoàn toàn đối lập nhau", "C. Vì nâng cao sức khỏe chỉ là một phần rất nhỏ của TT-GDSK", "D. Vì chúng không có liên quan gì đến nhau"], "ans": "A"},
    {"q": "Câu 48. Một địa phương chỉ tập trung xây dựng chính sách y tế công cộng mà bỏ qua phát triển kỹ năng cá nhân và tạo môi trường hỗ trợ thì theo mô hình Ottawa, chương trình đó:", "ops": ["A. Đầy đủ và toàn diện", "B. Chưa toàn diện vì thiếu các thành tố phối hợp cần thiết", "C. Không cần các thành tố khác", "D. Không liên quan đến nguyên tắc lồng ghép"], "ans": "B"},
    {"q": "Câu 49. Trong lý thuyết phổ biến sự đổi mới, nhóm 'đa số muộn' so với nhóm 'khởi xướng' có đặc điểm gì?", "ops": ["A. Chấp nhận cái mới sớm hơn nhóm khởi xướng", "B. Chấp nhận cái mới chậm hơn, thận trọng hơn so với nhóm khởi xướng và đa số sớm", "C. Không bao giờ chấp nhận cái mới", "D. Là nhóm quyết định đầu tiên trong cộng đồng"], "ans": "B"},
    {"q": "Câu 50. Để một chương trình TT-GDSK đạt hiệu quả bền vững, cần phối hợp đồng thời những nguyên tắc/nội dung nào?", "ops": ["A. Chỉ cần áp dụng nguyên tắc trực quan", "B. Chỉ cần xây dựng chính sách công cộng lành mạnh", "C. Kết hợp các nguyên tắc TT-GDSK (khoa học, đại chúng, trực quan, thực tiễn, lồng ghép) với các nội dung nâng cao sức khỏe (chính sách, môi trường hỗ trợ, hành động cộng đồng, kỹ năng cá nhân, định hướng dịch vụ)", "D. Chỉ cần sự chỉ đạo của tuyến trung ương"], "ans": "C"}
]

# --- QUẢN LÝ TRẠNG THÁI (SESSION STATE) ---
if 'answers' not in st.session_state:
    st.session_state.answers = [None] * len(quiz_data)

# --- THIẾT KẾ SIDEBAR MENU ---
st.sidebar.title("📌 Mục lục phân đoạn")
menu = st.sidebar.radio("Chuyển nhanh tới mức độ:", [
    "Mức độ Dễ (Câu 1–15)", 
    "Mức độ Trung bình (Câu 16–35)", 
    "Mức độ Khó (Câu 36–50)"
])

# --- GIAO DIỆN CHÍNH ---
st.title("📢 TRẮC NGHIỆM TRUYỀN THÔNG - GDSK")
st.caption("Ứng dụng tự động chấm điểm thực thời bám sát cấu trúc của tệp 'Bo_50_cau_trac_nghiem_TT-GDSK.docx'")
st.markdown("---")

def render_quiz_block(start_idx, end_idx):
    for i in range(start_idx, end_idx):
        item = quiz_data[i]
        saved_idx = st.session_state.answers[i]
        
        # Tạo widget nút trắc nghiệm dạng hàng ngang (horizontal)
        user_choice = st.radio(
            item["q"], 
            item["ops"], 
            index=saved_idx, 
            key=f"mcq_{i}", 
            horizontal=True
        )
        
        if user_choice is not None:
            # Lưu lại trạng thái đáp án vừa chọn
            st.session_state.answers[i] = item["ops"].index(user_choice)
            
            # Cắt ký tự chữ cái đầu tiên (A, B, C, D) từ chuỗi phương án để đối chiếu đáp án chính xác
            if user_choice[0] == item["ans"]:
                st.success(f"✅ Đúng! Đáp án chính xác là: **{item['ans']}**")
            else:
                st.error(f"❌ Chưa chính xác. Đáp án đúng là: **{item['ans']}**")
        st.markdown("<hr style='margin: 10px 0px; border-top: 1px dashed #bbb;'>", unsafe_allow_html=True)

# Điều hướng render theo phân đoạn sidebar để tối ưu scannable
if menu == "Mức độ Dễ (Câu 1–15)":
    st.subheader("🟢 PHẦN I — MỨC ĐỘ DỄ")
    render_quiz_block(0, 15)

elif menu == "Mức độ Trung bình (Câu 16–35)":
    st.subheader("🟡 PHẦN II — MỨC ĐỘ TRUNG BÌNH")
    render_quiz_block(15, 35)

elif menu == "Mức độ Khó (Câu 36–50)":
    st.subheader("🔴 PHẦN III — MỨC ĐỘ KHÓ")
    render_quiz_block(35, 50)
