import shelve

# Mode
IS_SHELVE = True

# Separator
SEPARATOR = ' | *** | '


def get_links_list() -> list[str]:
    with open('links.txt', 'r') as f:
        return f.readlines()


def get_link(short_link: str, links: list[str]) -> list[str] | None:
    links_found = [l for l in links if l.startswith(f'{short_link.strip()}{SEPARATOR}')]

    if len(links_found):
        return links_found[0].split(SEPARATOR)
    else:
        return None


def add_link() -> None:
    """
    Add short and full links
    :return: None
    """
    # Input data
    short_link = input('Enter short URL: ')
    full_link = input('Enter full URL: ')

    # Check empty
    is_links = short_link and short_link.strip() and full_link and full_link.strip()

    if is_links:

        # Check separator
        is_links_not_contain_separator = SEPARATOR not in short_link and SEPARATOR not in full_link

        if is_links_not_contain_separator:
            if not IS_SHELVE:
                # 1
                links = get_links_list()

                link = get_link(short_link, links)

                if not link:
                    with open('links.txt', 'a') as f:
                        # Store link to file
                        f.write(f'{short_link.strip()}{SEPARATOR}{full_link.strip()}\n')
                        print('Link was successfully added!')
                else:
                    # Error
                    print(f'Key {short_link.strip()} already exists!')
            else:
                # 2
                with shelve.open('links-shelve') as links:
                    if short_link.strip() not in links:
                        links[short_link.strip()] = full_link.strip()
                        print('Link was successfully added!')
                    else:
                        # Error
                        print(f'Key {short_link.strip()} already exists!')


        else:
            # Error
            print(f'Short and Full URLs cannot contain «{SEPARATOR}»')

    else:
        # Error
        print('Short and Full URLs must not be empty.')


def show_full_link_by_short_link() -> None:
    """
    Show full link by short link
    :return: None
    """
    short_link = input('Enter short URL: ')

    if short_link and short_link.strip():
        if not IS_SHELVE:
            # 1
            links = get_links_list()

            link = get_link(short_link, links)

            print(link[1], end='')
        else:
            # 2
            with shelve.open('links-shelve') as links:
                link = links[short_link.strip()]

            print(link)
    else:
        print(f'Short URL does not exist.')


def show_links() -> None:
    """
    Show list of links
    :return: None
    """
    if not IS_SHELVE:
        # 1
        links = get_links_list()

        for index, link in enumerate(links):
            link = link.split(SEPARATOR)

            print(f'{index + 1}. {link[0]}: {link[1]}', end='')
    else:
        # 2
        with shelve.open('links-shelve') as links:
            for index, link in enumerate(links.items()):
                print(f'{index + 1}. {link[0]}: {link[1]}')
