from ..main import add_link, show_full_link_by_short_link, show_links


def menu() -> None:
    while True:
        choice = input(
            'MENU\n'
            '\t1. Add new link\n'
            '\t2. Show link by short URL\n'
            '\t3. Show all full links\n'
            '\t4. Exit\n'
            'Your choice is: '
        )

        match choice:
            case '1':
                add_link()
            case '2':
                show_full_link_by_short_link()
            case '3':
                show_links()
            case '4':
                break
            case _:
                print('Invalid choice.')
