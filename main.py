import asyncio
from src import Drom, Brand


async def main() -> None:
    brand: str

    # ask to enter car brand
    brand = input(Brand.question.value)
    # ask brand until it exists
    while not await Drom.check_brand(brand):
        print(Brand.error.value)
        # ask to provide car brand
        brand = input(Brand.question.value)
    # parse all the cars under this brand
    await Drom.parse(brand)

    return


if __name__ == '__main__':
    asyncio.run(main())
