# flat than nested
import ch_02_foundations._07_flat_support_file as s
def main():

    download_flat()


def download_flat():

    print('Lets try to downnload the file')

    if not s.check_download_url():
        print('Bad url')
        return

    if not  s.check_network():
        print('No network')
        return

    if not s.check_dns():
        print('No DNS')
        return

    if not s.check_access_allowed():
        print('No access')

    print("Swwt you can download")


if __name__ == '__main__':
    main()