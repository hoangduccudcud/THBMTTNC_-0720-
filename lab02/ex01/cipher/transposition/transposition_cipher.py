class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        """
        Mã hóa văn bản bằng thuật toán mã hóa chuyển vị cột.

        Args:
            text (str): Văn bản gốc cần mã hóa.
            key (int): Khóa (số cột) để mã hóa.

        Returns:
            str: Văn bản đã mã hóa.
        """
        encrypted_text = ''
        # Duyệt qua từng "cột"
        for col in range(key):
            pointer = col
            # Lấy các ký tự từ văn bản gốc theo thứ tự cột
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key  # Di chuyển đến ký tự tiếp theo trong cùng cột
        return encrypted_text

    def decrypt(self, text, key):
        """
        Giải mã văn bản bằng thuật toán mã hóa chuyển vị cột.

        Args:
            text (str): Văn bản đã mã hóa cần giải mã.
            key (int): Khóa (số cột) đã được sử dụng để mã hóa.

        Returns:
            str: Văn bản đã giải mã.
        """
        # Tính số hàng của ma trận giả định
        num_rows = (len(text) + key - 1) // key # làm tròn lên

        # Tính số ô "trống" ở cuối hàng cuối cùng
        num_shaded_boxes = (num_rows * key) - len(text)

        # Khởi tạo một danh sách để chứa các cột đã giải mã
        # Mỗi phần tử trong danh sách này sẽ là một chuỗi đại diện cho một cột
        # và sẽ được điền vào sau
        decrypted_cols = [''] * key

        row, col = 0, 0
        # Duyệt qua từng ký tự trong văn bản đã mã hóa
        for symbol in text:
            # Gán ký tự vào vị trí cột hiện tại
            decrypted_cols[col] += symbol
            col += 1

            # Nếu đã điền đủ số ký tự cho cột hiện tại
            # Hoặc nếu đang ở cột cuối cùng và đã điền hết các ô không bị "che"
            if col == key or \
               (col == key - 1 and row >= num_rows - 1 - num_shaded_boxes):
                col = 0 # Đặt lại cột về 0 để chuyển sang hàng tiếp theo
                row += 1 # Tăng hàng

        # Nối các cột lại để tạo thành văn bản giải mã
        # Duyệt qua từng hàng để đọc lại văn bản gốc
        decrypted_text_list = [''] * len(text)
        current_index = 0
        for r in range(num_rows):
            for c in range(key):
                if c < len(decrypted_cols) and r < len(decrypted_cols[c]):
                    decrypted_text_list[r * key + c] = decrypted_cols[c][r]
                    current_index += 1
        
        # Phần giải mã trong ảnh có vẻ đang cố gắng xây dựng lại
        # nhưng cách tiếp cận này khó hơn.
        # Dựa vào cách mã hóa, để giải mã, ta cần xây dựng lại ma trận
        # rồi đọc theo hàng.
        
        # Sửa lại phần giải mã để nó khớp với cách mã hóa (đọc theo cột).
        # Cách đọc đúng là: decrypted_text[col][row]
        # Ví dụ: text = "HAYCHAO", key = 3
        # Ma trận mã hóa:
        # H C O
        # A H A
        # Y
        # encrypted = "HAYCHAO"
        # decrypt(encrypted, 3)
        # num_rows = (7 + 3 - 1) // 3 = 3
        # num_shaded_boxes = (3 * 3) - 7 = 2 (tại cột 1 và 2 của hàng 2)
        # encrypted: H A Y C H A O
        # col_lengths: H A Y (3), C H (2), A O (2)
        # (cột 0, 1, 2)
        # decrypted_cols[0] = "HAY"
        # decrypted_cols[1] = "CH"
        # decrypted_cols[2] = "AO"

        # Để giải mã, chúng ta phải đọc lại theo hàng:
        # H C A
        # A H O
        # Y
        # => "HCA AHO Y" (không đúng)

        # Logic giải mã đúng là:
        # Khởi tạo một danh sách các chuỗi, mỗi chuỗi đại diện cho một hàng
        # Sau đó điền các ký tự vào từng hàng.
        # Phần `decrypted_text = [''] * key` trong ảnh là sai, nó phải là
        # `decrypted_text = [''] * len(text)` để chứa kết quả cuối cùng.
        # Và phần `decrypted_text[col] += symbol` cũng sai vì nó thêm vào cột
        # trong khi chúng ta cần xây dựng lại theo hàng.

        # Logic giải mã phổ biến hơn:
        # Tính số hàng và số cột
        num_columns = key
        num_rows = (len(text) + num_columns - 1) // num_columns # Round up

        # Tính số ô trống ở cuối ma trận giả định
        num_empty_cells = (num_columns * num_rows) - len(text)

        # Tạo một ma trận rỗng để điền vào
        # (Mỗi phần tử là một ký tự rỗng, hoặc có thể là None)
        decryption_grid = [[''] * num_columns for _ in range(num_rows)]

        current_char_index = 0
        # Điền các ký tự đã mã hóa vào ma trận theo cột
        for col in range(num_columns):
            for row in range(num_rows):
                # Bỏ qua các ô "trống" ở cuối ma trận
                if (col >= num_columns - num_empty_cells) and (row == num_rows - 1):
                    continue
                
                if current_char_index < len(text):
                    decryption_grid[row][col] = text[current_char_index]
                    current_char_index += 1

        # Đọc các ký tự từ ma trận theo hàng để tạo văn bản giải mã
        decrypted_message = []
        for row in range(num_rows):
            for col in range(num_columns):
                if decryption_grid[row][col] != '': # Chỉ thêm các ô đã được điền
                    decrypted_message.append(decryption_grid[row][col])
        
        return ''.join(decrypted_message)