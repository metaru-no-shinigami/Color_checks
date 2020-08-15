import requests

url_input = str(input("API url string:"))
url = "https://api.scryfall.com/" + url_input
Saga = requests.get(url)
Saga_json = Saga.json()
w = 0
u = 0
b = 0
r = 0
g = 0
c = 0
for s in Saga_json['data']:
    C = s['color_identity']
    w += 1 * bool(C == ['W'])
    u += 1 * bool(C == ['U'])
    b += 1 * bool(C == ['B'])
    r += 1 * bool(C == ['R'])
    g += 1 * bool(C == ['G'])
    c += 1 * bool(C == [])


t = int(Saga_json['total_cards'])

print("___________________________________")
print("White:", w, "(", 100*w/t, "%", ")")
print("Blue:", u, "(", 100*u/t, "%", ")")
print("Black:", b, "(", 100*b/t, "%", ")")
print("Red:", r, "(", 100*r/t, "%", ")")
print("Green:", g, "(", 100*g/t, "%", ")")
print("Colorless:", c, "(", 100*c/t, "%", ")")
print("Total:", t)
print("___________________________________")




