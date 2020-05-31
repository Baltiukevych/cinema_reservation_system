def card_printer(client, seat, movie_number, cinema_plan):
    text = f"| Client: {client} | seat: {seat} | Movie Number: {movie_number} | cinema: {cinema_plan} |"
    frame = f"+{'-' * (len(text) - 2)}+"
    frame_empty = f"|{' ' * (len(text) - 2)}|"

    border = [frame, frame_empty, text, frame_empty, frame]
    banner = "\n".join(border)
    print(banner)
    print(border)
    print(text)
    print(frame)