import os
from Entities import Navigator, Query, Result


def main():
    run_gui()
    # run_in_console()
    # calculate_avg()


def run_gui():
    os.environ["KIVY_NO_CONSOLELOG"] = "1"
    from GUI import NavigatorApplication
    navigator = NavigatorApplication()
    navigator.run()


def run_in_console():
    map_path = './input/Map200k.txt'
    query_path = './input/Query_200k_1000.txt'
    output_path = './output'
    need_generate_map = False
    plot_all_nodes = True

    results = []
    navigator = Navigator(map_path)
    queries = Query.read_queries(query_path)

    for i, query in enumerate(queries):
        result = navigator.navigate(query)
        if need_generate_map:
            result.generate_map(output_path, plot_all_nodes)
        results.append(result)
        print(result)
        print('\n========================================================================================\n')

    return results


def calculate_avg():
    map_path = './input/Map200k.txt'
    query_path = './input/Query_200k_1000.txt'
    count = 100

    navigator = Navigator(map_path)
    queries = Query.read_queries(query_path)

    total_count = 0
    total_time = 0
    for i, query in enumerate(queries):
        print(f'Query: {i}\tCount: {total_count}')
        if total_count == count:
            break
        result = navigator.navigate(query)
        if result.reason == Result.REASON_SUCCESS:
            total_count += 1
            total_time += result.exec_time

    avg = total_time / total_count
    print(f'Average execution time for {count} samples is: {avg} s')
    return avg


if __name__ == '__main__':
    main()
