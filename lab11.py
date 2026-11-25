# Intermediate programming practice: async and sockets.
#
# For EACH problem, work out your problem-solving OUTLINE first, then implement it (you
# may use an AI assistant to help - see the README). The async parts must actually run
# their work CONCURRENTLY (that's the whole point), not one after another.
#
# Do not rename the functions - the tests use these names.

import asyncio
import socket


async def gather_doubled(numbers):
    # Outline (write your plan here first):
    # give a list multiply each element by 2, concurrently
    # i.e [5,6,7] = [10,12,14]
    # basically just put two functions in one, one for the mini problem thats just take all emenets multiply by 2, and then shove it into the otehr function that calls it concurrently awaito or whatever

    # TODO (Part 1, async): run one async task per number that returns n * 2, all
    #   CONCURRENTLY with asyncio.gather, and return the results as a list in the same
    #   order as `numbers`.

    async def double(n):
        return n * 2

    return await asyncio.gather(*[double(n) for n in numbers])

async def fastest(jobs):
    # Outline:
    # have a key pairs of label delay, run them all at same time and then give the one thats first to finish
    # i.e jobs = [("slow", 3), ("fast", 1), ("medium", 2)], gives fast
    # wait amount of time given for each delay given as function, run each concurently with that function, give the first one that completes and give that
    # TODO (Part 2, async): `jobs` is a list of (label, delay) pairs. Start them all
    #   concurrently - each one just does `await asyncio.sleep(delay)` - and return the
    #   label of the FIRST job to finish. (Hint: asyncio.as_completed.)
    async def run(label, delay):
        await asyncio.sleep(delay)
        return label

    tasks = [asyncio.create_task(run(label, delay)) for label, delay in jobs]

    for next_done in asyncio.as_completed(tasks):
        winner = await next_done
        break  # we only want the first one


    return winner


def echo_once(host, port, message):
    # Outline:
    # as a client open the suff needed to sent to server, get server reply and give it as a string
    # i.e host = "localhost", port = 12345, message = "Hello" would give back "Hello" as a string
    # create socket with afnet and sock stream, connect host and port to server, send all as bytes, read and decode server reply

    # TODO (Part 3, sockets): open a TCP socket and connect to (host, port). Send
    #   `message` (encode it to bytes first), receive the server's reply, and return it
    #   as a string. (Hint: socket.socket, .connect, .sendall, .recv, .decode.)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))        
        sock.sendall(message.encode())  
        reply = sock.recv(1024)    
    return reply.decode() 


def main():
    # Optional scratch space - try the async parts here, e.g.:
    print(asyncio.run(gather_doubled([1, 2, 3, 4])))   # [2, 4, 6, 8]
    


if __name__ == "__main__":
    main()
