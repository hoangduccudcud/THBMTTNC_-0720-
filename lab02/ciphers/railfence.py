class RailFenceCipher:
    def encrypt_text(self, text, rails):
        rail = [['\n' for _ in range(len(text))] for _ in range(rails)]
        dir_down = False
        row, col = 0, 0

        for char in text:
            if row == 0 or row == rails - 1:
                dir_down = not dir_down
            rail[row][col] = char
            col += 1
            row += 1 if dir_down else -1

        result = []
        for i in range(rails):
            for j in range(len(text)):
                if rail[i][j] != '\n':
                    result.append(rail[i][j])
        return "".join(result)

    def decrypt_text(self, text, rails):
        rail = [['\n' for _ in range(len(text))] for _ in range(rails)]
        dir_down = None
        row, col = 0, 0

        # Đánh dấu vị trí trong ma trận
        for _ in range(len(text)):
            if row == 0:
                dir_down = True
            if row == rails - 1:
                dir_down = False
            rail[row][col] = '*'
            col += 1
            row += 1 if dir_down else -1

        # Điền ký tự vào ma trận
        index = 0
        for i in range(rails):
            for j in range(len(text)):
                if rail[i][j] == '*' and index < len(text):
                    rail[i][j] = text[index]
                    index += 1

        # Đọc ma trận để giải mã
        result = []
        row, col = 0, 0
        for _ in range(len(text)):
            if row == 0:
                dir_down = True
            if row == rails - 1:
                dir_down = False
            if rail[row][col] != '\n':
                result.append(rail[row][col])
                col += 1
            row += 1 if dir_down else -1
        return "".join(result)