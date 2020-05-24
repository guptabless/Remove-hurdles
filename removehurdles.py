import bcolors
import sys, argparse

def banner():
    print("""


██████╗░███████╗███╗░░░███╗░█████╗░██╗░░░██╗███████╗░░░░░░██╗░░██╗██╗░░░██╗██████╗░██████╗░██╗░░░░░███████╗░██████╗
██╔══██╗██╔════╝████╗░████║██╔══██╗██║░░░██║██╔════╝░░░░░░██║░░██║██║░░░██║██╔══██╗██╔══██╗██║░░░░░██╔════╝██╔════╝
██████╔╝█████╗░░██╔████╔██║██║░░██║╚██╗░██╔╝█████╗░░█████╗███████║██║░░░██║██████╔╝██║░░██║██║░░░░░█████╗░░╚█████╗░
██╔══██╗██╔══╝░░██║╚██╔╝██║██║░░██║░╚████╔╝░██╔══╝░░╚════╝██╔══██║██║░░░██║██╔══██╗██║░░██║██║░░░░░██╔══╝░░░╚═══██╗
██║░░██║███████╗██║░╚═╝░██║╚█████╔╝░░╚██╔╝░░███████╗░░░░░░██║░░██║╚██████╔╝██║░░██║██████╔╝███████╗███████╗██████╔╝
╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝░╚════╝░░░░╚═╝░░░╚══════╝░░░░░░╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═════╝░╚══════╝╚══════╝╚═════╝░
                                                                                                        Code by NG          
          """)
count = 0

if len(sys.argv) > 1:
    banner()
    if ((sys.argv[1] == '-l1') | (sys.argv[1] == '-l2')):
        try:
            input_file = sys.argv[2]
            out_file = sys.argv[4]

            parser = argparse.ArgumentParser()
            parser.add_argument("-l1", required=True)
            parser.add_argument("-l2", required=True)
            args = parser.parse_args()

            f = open(input_file, 'r')
            lines = f.read().split("\n")
            print(bcolors.BLUE)
            for i in lines:
                count = count + 1

            f1 = open(input_file, 'a+')
            if len(lines) == count:
                lines.append('')
                f1.close()

            line_visible = set()
            out_file = open(out_file, "w")
            for line in open(input_file, "r"):
                 if line not in line_visible:
                    out_file.write(line)
                    line_visible.add(line)
                    line.rstrip(line)
            print(bcolors.OKMSG, 'Output saved in specified location')

        except:
            print('Please enter python removehurdles.py -l1 <valid path of input file > -l2 <output location for saved location>')

    elif ((sys.argv[1] == '-h') | (sys.argv[1] == '--help')):
        print(bcolors.BOLD + 'usage: removehurdles.py [-h] -l1 Location' '\n' 'OPTIONS:' '\n' '-h,--help    '
                             'show this help message and exit' '\n''-l1 Location,   --location Location' '\n' '-l2 Output    Output File location')
    elif (((sys.argv[1] != '-l1') | (sys.argv[1] != '-l2'))):
        print(bcolors.ERR + 'Please enter -l1 <valid 1st input location of file > -l2 <valid output location to save file>')
else:
    banner()
    print(bcolors.ERR + 'Please select atleast 1 option from (-l1,-l2) or -h, with a valid path location of files')
