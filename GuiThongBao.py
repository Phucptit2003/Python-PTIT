# Đọc số bộ test
T = int(input())

# Xử lý từng bộ test
for _ in range(T):
    message = input()
    if len(message) <= 100:
        print(message)
    else:
        truncated_message = message[:100]
        
        if message[100].isspace():
            print(truncated_message)
        else:
            last_space_index = truncated_message.rfind(' ')
            
            if last_space_index != -1:
                truncated_message = truncated_message[:last_space_index]
            
            print(truncated_message)
