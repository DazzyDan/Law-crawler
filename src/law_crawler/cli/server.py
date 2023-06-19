import argparse
import sys
import os
from law_crawler.app import LawCrawlerApp


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser(description="Law Crawler Server")
    parser.add_argument("--ip", "-i", default="0.0.0.0", help="Ip to be binded to")
    parser.add_argument("--port", "-p", default=8080, help="Port to be listened")
    parser.add_argument("--debug", "-d", action="store_true", help="Enable debug")
    args = parser.parse_args(argv)
    app = LawCrawlerApp()
    app.run(host=args.ip, port=args.port, debug=args.debug)


if __name__ == "__main__":
    main()
