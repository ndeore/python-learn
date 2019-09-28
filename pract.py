GRAND_TOTAL =1000

def get_receieved_marks():
    return int(input(
        'Enter Received Marks: '
    ))

def calculate_percentage(recieved_marks):
    if recieved_marks <= 0:
        return None
    else:
        return (recieved_marks / GRAND_TOTAL ) * 100

if __name__ == '__main__':
    # Changes in B branch
    recieved_marks = get_receieved_marks()
    perc = calculate_percentage(recieved_marks)

    if perc is not None:
        print('Percentage is %s' % str(perc))
    else:
        print('Input marks were invalid')