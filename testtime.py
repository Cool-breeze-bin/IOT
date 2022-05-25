import cv2
import datetime
def cvcamera():
    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    cap.set(10,100)

    while True:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
def parse_expenses():
    """Parse the list of expenses and return the list of triples (date, value, currency).
        Ignore lines starting with #.
        Parse the date using datetime.
        Example expenses_string:
            2016-01-02 -34.01 USD
            2016-01-03 2.59 DKK
            2016-01-03 -2.72 EUR
        """
    expenses_string = """2016-01-02 -34.01 USD
2016-01-03 2.59 DKK
2016-01-03 -2.72 EUR"""
    expenses = []
    for line in expenses_string.splitlines():
        if line.startswith('#'):
            continue
        date, value, currency = line.split()
        date = datetime.datetime.strptime(date, '%Y-%m-%d')
        value = float(value)
        expenses.append((date, value, currency))
    return expenses

def main():
    cvcamera()
    expenses = parse_expenses()
    print(expenses)


if __name__ == '__main__':
    main()
