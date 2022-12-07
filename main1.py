''' cli tool fetch data from xkcd api "https://xkcd.com/" 
    python task_one.py --max 87  --any 15 '''

import argparse
from random import randint
from typing import List

def ran_gen(start: int=1, stop : int=87, limit : int=15) -> list[int]:
    '''
    args: 
        start:(int) first numeric value of range
        stop: (int) last numeric value of range
        limt: (int) num of results to yield
    
    retruns :
        list[int] : radom values in range(start:stop) with count limited to limit

    '''
    result = [randint(start, stop) for i in range(limit)]
    return result


if __name__ == "__main__":
    example = """example:
    
    python task_one.py --max 87  --any 15
    """
 
    parser = argparse.ArgumentParser(
        description="CLI tool to fetch resource(s) from API",
        epilog=example
    )
    parser.add_argument(
        "-m",
        "--max",
        type=int,
        default=87, # here we can set max num as we want eg -1000 
        help= "max num of resources to be fetch"
    )
    parser.add_argument(
        "-a",
        "--any",
        type=int,
        default=15, # we can set any num here eg - 1
        help="random sized chunck of resources to be fetched"
    )
 
    args = parser.parse_args()
    print(args.any)
    print(args.max)
    # print(ran_gen(1, args.max, args.any))
    comic_num = (ran_gen(1, args.max, args.any))
    print(comic_num)
    print(len(comic_num))
    print(parser.print_help())
