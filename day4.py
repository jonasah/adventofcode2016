
def rotate(l, n):
    return l[n:] + l[:n]

def calc_checksum(encrypted_name):
    occurrence = dict()
    name = encrypted_name.replace('-', '')

    for letter in name:
        if not letter in occurrence:
            occurrence[letter] = 0

        occurrence[letter] += 1

    f = sorted(occurrence.items(), key=lambda x: (-x[1], x[0]))

    checksum = ''

    for g in f:
        checksum += g[0]

    return checksum[:5]

def main():
    input_file = open('day4input.txt')
    rooms = input_file.readlines()
    input_file.close()

    sector_id_sum = 0
    real_rooms = []

    for room_line in rooms:
        room = room_line.strip()
        last_dash_index = room.rfind('-')
        first_bracket_index = room.find('[')

        encrypted_name = room[:last_dash_index]
        checksum = room[first_bracket_index+1:-1]

        if calc_checksum(encrypted_name) == checksum:
            sector_id = int(room[last_dash_index+1:first_bracket_index])
            sector_id_sum += sector_id
            real_rooms.append((encrypted_name, sector_id))

    print("Part 1:", sector_id_sum)

    alphabet = [chr(x) for x in range(ord('a'), ord('z')+1)]

    for room in real_rooms:
        encrypted_name = room[0]
        sector_id = room[1]

        actual_shifts = sector_id % len(alphabet)
        shifted_alphabet = rotate(alphabet, actual_shifts)

        real_name = ''

        for letter in encrypted_name:
            if letter == '-':
                real_name += ' '
            else:
                real_name += shifted_alphabet[ord(letter)-ord('a')]

        if real_name == 'northpole object storage':
            print("Part 2:", sector_id)
            break

if __name__ == '__main__':
    main()
