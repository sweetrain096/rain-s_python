import csv
lunch = {
    "특식" : "우삼겹 숙주볶음", 
    "한식" : "김치볶음밥, 계란후라이",
    "중간?": "부대찌개, 깐풍기"
}

with open("lunch.csv", "w") as f:
    for key, value in lunch.items():
        f.write(f"{key}, {value}\n")