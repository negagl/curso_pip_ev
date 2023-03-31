import matplotlib.pyplot as plt


def generate_pie_chart():
    labels = ['a', 'b', 'c']
    values = [200, 34, 500]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie_chart.png')
    plt.close()
