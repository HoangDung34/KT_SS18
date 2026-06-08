players_match = []

def check_exist_id(player, id):
    id = id.strip().upper()

    for human in player:
        if id == human['id']:
            return human
    return None

def hieu_xuat(match, victory, kien_tao):
    diem_hieu_xuat = (match * 1) + (victory * 3) + (kien_tao * 2)
    return diem_hieu_xuat
    
def check_stautus_player(score):
    if score < 15:
        return "Cần thanh lý / Cho mượn"
    elif 15 <= score < 30:
        return "Dự bị chiến lược"
    elif 30 <= score < 50:
        return "Trụ cột đội bóng"
    elif score >= 50:
        return "Ngôi sao đẳng cấp"


def display_player(player):
    if len(player) == 0:
        print("Danh sách rỗng !!!")
    else:
        print("--- DANH SÁCH CẤU THỦ ---")
        print("Mã cầu thủ | Họ và tên | Số trận thi đấu | Số trận thi đấu | Số bàn thắng | Số đường kiến tạo | Điểm hiệu xuất | Phân loại phong độ")
        print("---------------------------------------------------------------------------------------------------------------------------------------")

        for human in player:
            diem_hieu_xuat = hieu_xuat(human['number_match'], human['number_victory'], human['kien_tao'])
            status = check_stautus_player(diem_hieu_xuat)

            print(f"{human['id']} | {human['name']} | {human['number_match']} | {human['number_victory']} | {human['kien_tao']} | {diem_hieu_xuat} | {status}")

        print("---------------------------------------------------------------------------------------------------------------------------------------")

def add_player(player):
    while True:
        player_id = input("Nhập mã cầu thủ: ").strip().upper()

        if player_id == "":
            print("Mã không được để trống!!!")
            continue
        
        if check_exist_id(player, player_id):
            print("Mã cầu thủ đã tồn tại")
            continue

        break

    while True:
        name = input("nhập họ và tên cầu thủ: ").strip().title()

        if name == "":
            print("Tên không được để trống")
            continue
        break

    while True:
        try:
            match = int(input("Nhập số trận đấu: "))

            if match < 0:
                print("Không hợp lệ")
                continue
            break
        except:
            print("nhập đúng định dạng số")
            continue

    while True:
        try:
            victory = int(input("Nhập số bàn thắng: "))

            if victory < 0:
                print("Không hợp lệ")
                continue
            break
        except:
            print("Vui lòng nhập đúng định dạng số")
            continue

    while True:
        try:
            kien_tao = int(input("Nhập số đường tạo: "))

            if kien_tao < 0:
                print("Không hợp lệ")
                continue
            break
        except:
            print("Vui lòng nhập đúng định dạng số")
            continue

    diem_hieu_xuat = hieu_xuat(match, victory, kien_tao)

    status = check_stautus_player(diem_hieu_xuat)
        
    player.append({"id": player_id, "name": name, "number_match": match, "number_victory": victory, "kien_tao": kien_tao, "hieu_xuat": diem_hieu_xuat, "status": status})

    print("Tiếp nhận cầu thủ thành công")

def update_player(player):
    while True:
        search_id = input("Nhập id cần cập nhật: ").strip().upper()

        played = check_exist_id(player, search_id)

        if played is None:
            print("Cầu thủ không có trong danh sách")
            continue

        new_match = int(input("Nhập số trận đấu mới: "))
        new_victory = int(input("Nhập số bàn thắng mới: "))
        new_kien_tao = int(input("Nhập số kiến tạo mới: "))

        diem_hieu_xuat = hieu_xuat(new_match, new_victory, new_kien_tao)

        new_status = check_stautus_player(diem_hieu_xuat)

        played['number_match'] = new_match
        played['number_victory'] = new_victory
        played['kien_tao'] = new_kien_tao
        played['hieu_xuat'] = diem_hieu_xuat
        played['status'] = new_status
        break

def find_player(player):
    while True:
        search_id = input("Nhập id cần cập nhật: ").strip().upper()

        played = check_stautus_player(player, search_id)

        if played is None:
            print("Cầu thủ không có trong danh sách")
            continue

        print(player)
        return

def main():
    while True:
        try:
            choice = int(input("""
            1. Hiển thị danh sách cầu thủ
            2. Tiếp nhận cầu thủ mới
            3. Cập nhật thông tin và chỉ số
            4. Xóa cầu thủ (Thanh lý hợp đồng)
            5. Tìm kiếm cầu thủ
            6. Thống kê phân loại cầu phong độ
            7. Đánh giá phong độ tự dộng
            8. Thoát
            Chọn chức năng:
            """))
        except:
            print("Lựa chọn không hợp lệ, vui lòng chọn chức năng 1 - 7 !!!")
            continue

        match choice:
            case 1:
                display_player(players_match)
            case 2:
                add_player(players_match)
            case 3:
                update_player(players_match)
            case 5:
                find_player(players_match)
            case 8:
                print("Thoát chương trình")
                break
            case _:
                print("Lựa chọn không hợp lệ, vui lòng chọn chức năng 1 - 7 !!!")
main()