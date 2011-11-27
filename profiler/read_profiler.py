#!/usr/bin/env python
"""Read a profile file generated by hotshot

Can be used as: ./profile ./<file_name>
"""

import hotshot.stats
import sys

stats = hotshot.stats.load(sys.argv[1])

stats.sort_stats('time', 'calls')
stats.print_stats()
