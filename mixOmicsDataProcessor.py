import pandas as pd


def processMixOMicsData(csvFileLocation):

    df = None

    try:
        if csvFileLocation:
            df = pd.read_csv(csvFileLocation)
        else:
            print("Please provide a valid file location")
    except:
        print("File not found")

    try:
        allColumns = df.columns
        dropColumns = []

        for x in allColumns:
            columnValues = df[x].values
            totalCount = len(columnValues)
            negativeCount = 0
            for y in columnValues:
                if y < 0:
                    negativeCount = negativeCount + 1
            if (negativeCount / totalCount) * 100 > 70:
                dropColumns.append(x)

        df.drop(columns=dropColumns).to_csv("filteredData.csv", index=False)
    except:
        print("Not a valid data frame")


if __name__ == "__main__":
    processMixOMicsData(csvFileLocation="")
