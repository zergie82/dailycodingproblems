'''
Suppose we represent our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.

Note:

The name of a file contains at least a period and an extension.

The name of a directory or sub-directory will not contain a period.
'''

class Node:
    def __init__(self, val=None, level=None, parent=None, is_file=False):
        self.val = val
        self.level = level
        self.parent = parent
        self.subdir = list()
        self.is_file = is_file

    def add_node(self, node=None):
        self.subdir.append(node)

    def get_parent(self):
        return self.parent

    def __repr__(self):
        return self.val

class Tree:
    def __init__(self):
       self.root = Node('*', -1)

    def populate_tree(self, fs_string):
        fs_string = fs_string.split('\n')
        cur_root = self.root
        cur_level = self.root.level

        for part in fs_string:
            tabs = 0
            while part[tabs] == '\t':
                tabs += 1

            if cur_level >= tabs:
                i = cur_level - tabs + 1
                while i != 0:
                    cur_root = cur_root.get_parent()
                    i -= 1

            if len(part.split('.')) > 1:
                next_node = Node(part.strip(), tabs, cur_root, True)
            else:
                next_node = Node(part.strip(), tabs, cur_root)

            cur_root.add_node(next_node)
            cur_level = tabs
            cur_root = next_node

def longest_path(node):
    if node.is_file:
        return len(node.val)
    if len(node.subdir) == 0:
        return 0

    max_len = 0
    for sub in node.subdir:
        max_len = max(max_len, longest_path(sub))

    length = max_len if node.level < 0 else max_len + len(node.val) + 1
    return length

if __name__ == '__main__':
    p1 = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
    p2 = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
