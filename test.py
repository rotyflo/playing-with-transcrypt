my_button = document.getElementById('myButton')

def blow_up_input():
    my_string = document.getElementById('myString').value
    html = ''
    size = 12

    for char in my_string:
        html += f"<span style='font-size: {size}px'>{char}</span>"
        size += 4

    my_div = document.getElementById('myDiv')

    my_div.innerHTML = html


my_button.onclick = lambda: blow_up_input()