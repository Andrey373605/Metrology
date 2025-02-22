



if __name__ == '__main__':
    data = find_operands()

    df = pd.DataFrame(data, columns=['Оператор', 'Количество'])

    print(tabulate(df, headers='keys', tablefmt='pretty'))

