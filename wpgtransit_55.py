#!/usr/bin/env python
"""Example usage of terminaltables with colorclass.

Just prints sample text and exits.
"""

from __future__ import print_function

from colorclass import Color, Windows

from terminaltables import SingleTable



def route55_bus_schedule():
    """Return table string to be printed."""
    table_data = [
        [Color('Bus NO#'), Color('{red}Morning AM{/red}'), Color('{yellow}Afternoon PM{/yellow}')],
				[Color('{green}55 @ Morrow{/green}'), Color('07:28')	,Color('{red}01:06{/red}')],
				[Color('{green}55 @ Morrow{/green}'), Color('07:45')	,Color('{red}01:26{/red}')],
				[Color('{green}55 @ Morrow{/green}'), Color('07:34')	,Color('{red}01:45{/red}')],
				[Color('{green}55 @ Morrow{/green}'), Color('07:54')	,Color('{red}01:05{/red}')],
				[Color('{green}55 @ Morrow{/green}'), Color('07:43')	,Color('{red}02:25{/red}')],
				[Color('{green}55 @ Morrow{/green}'), Color('07:51')	,Color('{red}02:45{/red}')],
				[Color('{green}55 @ Morrow{/green}'), Color('07:59')	,Color('{red}03:24{/red}')],
				[Color('{green}55 @ Morrow{/green}'), Color('08:08')	,Color('{red}03:33{/red}')],
				[Color('{green}55 @ Morrow{/green}'), Color('08:08')	,Color('{red}03:45{/red}')],
				[Color('{green}55 @ Morrow{/green}'), Color('08:17')	,Color('{red}03:52{/red}')],
				[Color('{green}55 @ Morrow{/green}'), Color('08:19')	,Color('{red}04:02{/red}')],
				[Color('{green}55 @ Morrow{/green}'), Color('08:25')	,Color('{red}04:09{/red}')],
				[Color('{green}55 @ Morrow{/green}'), Color('08:31')	,Color('{red}04:16{/red}')],
				[Color('{green}55 @ Morrow{/green}'), Color('08:34')	,Color('{red}04:28{/red}')],
				[Color('{green}55 @ Morrow{/green}'), Color('08:44')	,Color('{red}04:37{/red}')],
				[Color('{green}55 @ Morrow{/green}'), Color('08:42')	,Color('{red}04:46{/red}')],
				[Color('{green}55 @ Morrow{/green}'), Color('08:50')	,Color('{red}04:54{/red}')],
				[Color('{green}55 @ Morrow{/green}'), Color('09:02')	,Color('{red}05:04{/red}')],
				[Color('{green}55 @ Morrow{/green}'), Color('09:26')	,Color('{red}05:12{/red}')],
				[Color('{green}55 @ Morrow{/green}'), Color('09:46')	,Color('{red}05:22{/red}')],
				[Color('{green}55 @ Morrow{/green}'), Color('10:06')	,Color('{red}05:36{/red}')],
				[Color('{green}55 @ Morrow{/green}'), Color('10:26')	,Color('{red}05:54{/red}')],
				[Color('{green}55 @ Morrow{/green}'), Color('10:46')	,Color('{red}06:13{/red}')],
				[Color('{green}55 @ Morrow{/green}'), Color('11:06')	,Color('{red}06:31{/red}')],
				[Color('{green}55 @ Morrow{/green}'), Color('11:26')	,Color('{red}06:45{/red}')],
				[Color('{green}55 @ Morrow{/green}'), Color('11:46')	,Color('{red}07:07{/red}')],
				[Color('{green}55 @ Morrow{/green}'), Color('12:06')	,Color('{red}07:26{/red}')],
				[Color('{green}55 @ Morrow{/green}'), Color('12:26')	,Color('{red}07:43{/red}')],
				[Color('{green}55 @ Morrow{/green}'), Color('12:46')	,Color('{red}08:03{/red}')],
				[Color('{green}55 @ Morrow{/green}'), Color('') ,Color('{red}08:32{/red}')],
				[Color('{green}55 @ Morrow{/green}'), Color('') ,Color('{red}08:56{/red}')],
				[Color('{green}55 @ Morrow{/green}'), Color('') ,Color('{red}09:11{/red}')],
				[Color('{green}55 @ Morrow{/green}'), Color('') ,Color('{red}09:37{/red}')],
				[Color('{green}55 @ Morrow{/green}'), Color('') ,Color('{red}09:59{/red}')],
				[Color('{green}55 @ Morrow{/green}'), Color('') ,Color('{red}10:37{/red}')],
				[Color('{green}55 @ Morrow{/green}'), Color('') ,Color('{red}11:02{/red}')],
				[Color('{green}55 @ Morrow{/green}'), Color('') ,Color('{red}11:28{/red}')],

    ]
    table_instance = SingleTable(table_data, '55 Bus TimeTable LOl')
    table_instance.inner_heading_row_border = False
    table_instance.inner_row_border = True
    table_instance.justify_columns = {0: 'center', 1: 'center', 2: 'center'}
    return table_instance.table



def main():
    """Main function."""
    Windows.enable(auto_colors=True, reset_atexit=True)  # Does nothing if not on Windows.

    # print the above table
    print(route55_bus_schedule())
    print()

    # Credit section.
    table_instance = SingleTable([['Data Collected from WinnipegTransit']], 'Credit')
    print(table_instance.table)
    print()


if __name__ == '__main__':
    main()
