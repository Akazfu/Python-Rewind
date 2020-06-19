if __name__ == "__main__":
    # height_xiaoming, n = map(lambda i: int(i), sys.stdin.readline().split())
    # height_friends = [int(i) for i in sys.stdin.readline().split()]
    height_xiaoming, n = 90, 13
    height_friends = [100, 90, 91, 93, 109, 101, 95, 89, 87, 84, 88, 90, 84]
    height_friends.sort()

    difference = []
    result = []

    for friend in height_friends:
        difference.append(abs(friend - height_xiaoming))

    zipped = zip(difference, height_friends)
    sorted_zipped = sorted(zipped, key=lambda x: x[0])
    output_list = [y for x, y in sorted_zipped]
    output_list = [str(i)+' ' for i in output_list]
    output = ''.join(output_list)
    print(output)
