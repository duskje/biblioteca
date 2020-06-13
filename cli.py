import click
import library3

@click.group()
def main():
    pass

@main.command()
def list(): # why does this work? the click decorator maybe?
    babel = library3.Library()
    babel.load()

    book_list = []
    for book in babel.books:
        line = str(book)

        if not book.is_here:
            line += f' Return date: {book.date_lent}'

        book_list.append(line)

    print('\n'.join(book_list))
    babel.save()

@main.command()
@click.option('-t', '--title', required=True)
@click.option('-a', '--author')
@click.option('-y', '--year')
def add(title, author, year):
    babel = library3.Library()
    babel.load()

    babel.add_book(title, author, year)

    babel.save()

@main.command()
@click.option('-t', '--title', required=True)
def remove(title):
    babel = library3.Library()
    babel.load()

    babel.remove_book(title)

    babel.save()


@main.command()
@click.option('-t', '--title', required=True, multiple=True)
def lend_book(title):
    babel = library3.Library()
    babel.load()

    babel.lend_book(title)

    babel.save()

@main.command()
@click.option('-t', '--title', required=True, multiple=True)
def return_book(title):
    babel = library3.Library()
    babel.load()

    babel.return_book(title)

    babel.save()


if __name__ == '__main__':
    main()