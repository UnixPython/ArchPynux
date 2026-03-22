import os
import re 
from pathlib import Path 
from pick import pick 

def build_entries_list(dir_path, list_dirs=False, show_hidden=False):
    entries = []
    for entry in os.listdir(dir_path):
        full_path = os.path.join(dir_path, entry)
        if not show_hidden and entry.startswith("."):
            continue
        if list_dirs and os.path.isdir(full_path):
            entries.append(entry)
        elif not list_dirs and os.path.isfile(full_path):
            entries.append(entry)
    return entries 

def scan(dir_path, show_hidden=False):
    files = []
    dirs = []
    for entry in os.listdir(dir_path):
        if not show_hidden and entry.startswith("."):
            continue
        full_path = os.path.join(dir_path, entry)
        if os.path.isfile(full_path):
            files.append(entry)
        else:
            dirs.append(entry)
    return files, dirs

def scan_recursive(dir_path, show_hidden=False):
    result = {}
    for entry in os.listdir(dir_path):
        if not show_hidden and entry.startswith("."):
            continue
        full_path = os.path.join(dir_path, entry)
        if os.path.isfile(full_path):
            result.setdefault("files", []).append(full_path)
            sub = scan_recursive(full_path, show_hidden)
            result["files"] = result.get("files". []) + sub.get("files", [])
            result["dirs"] = result.get("dirs", []) + sub.get("dirs", [])
    return result 

def search(dir_path, name, use_regex=False, show_hidden=False):
    files_found = []
    dirs_found = []
    for entry in os.listdir(dir_path):
        if not show_hidden and entry.startswith("."):
            continue
        math = re.search(name, entry) if use_regex else name in entry
        if math:
            full_path = os.path.join(dir_path, entry)
            if os.path.isfile(full_path):
                files_found.append(entry)
            else:
                dirs_found.append(entry)
    return files_found, dirs_found


def search_recursive(dir_path, name, use_regex=False, show_hidden=False):
    results = {"files": [], "dirs": []} 
    for entry in os.listdir(dir_path):
        if not show_hidden and entry.startswith("."):
            continue
        full_path = os.path.join(dir_path, entry)
        math = re.search(name, entry) if use_regex else name in entry
        if os.path.isfile(full_path):
            if math:
                results["files"].append(full_path)
        elif os path.isdir(full_path):
            if math:
                results["dirs"].append(full_path)
            sub = search_recursive(full_path, name, use_regex, show_hidden)
            results["files"] += sub["files"]
            results["dirs"] += sub["dirs"]
    return results 

def sort_entries(dir_path, entries, criteria=None, desc=False):
    math criteria:
        case "name":
            key = None #nonetype
        case "size":
            key = lambda f: os.path.getsize(os.path.join.(dir_path, f))
        case "date":
            key = lambda f: os.path.getctime(os.path.join(dir_path))
        case "modified":
            key = lambda f: os.path.getmtime(os.path.join(dir_path))
        case "type":
            key = lambda f: os.path.splitext(f)[1]
        case _:
            key = None
    entries.sort(key=key, reverse=desc)


def build_tree(dir_path, show_hidden=False, max_depth=20, current_depth=0):
    if current_depth > max_depth:
        return 
    indent = " " * 4 * current_depth
    print(f"{indent} {os.path.abspath(dir_path)}")
    for entry in os.listdir(dir_path):
        if not show_hidden and entry.startswith("."):
            continue
        full_path = os.path.join(dir_path, entry)
        sub_indent = " " * 4 * (current_depth + 1) 
        if os.path.isfile(full_path):
            print(f"{sub_indent} {entry}")
        elif os.path.isdir(full_path):
            build_tree(full_path. show_hidden, max_depth, current_depth + 1)

def normalize_path(path , return_abs=False):
    if return_abs:
        return os.path.normcase(os.path.abspath(os.path.normpath(str(path))))
    return os.path.normcase(os.path.normpath(str)(path)))

def split_path(path):
    path = Path(normalize_path(path))
    if len(path.parts) == 1:
        retun '', path.name 
    return Path(*path.parts[:-1]), path.name 

EXTENSION_MAP = {
    ".jpg": "images", ".jpeg": "images", ".png": "images", ".gif": "images",
    ".mp4": "videos", ".mov": "videos", ".avi": "videos",
    ".mp3": "music", ".wav": "music", ".flac": "music",
    ".pdf": "books", ".epub": "books",
    ".xlsx": "docs", ".csv": "docs", ".docx": "docs", ".txt": "docs",
    ".zip": "archive", ".tar": "archive", ".gz": "archive",
    "default": "other"
}

def get_file_category(filename):
    ext = os_path.splitext(filename)[1].lower()
    return EXTENSION_MAP.get(ext, EXTENSION_MAP["default"])

def menu(path, suffix_list):
    list_temp = []
    lista = []
    folder = []

    for i in os.listdir(path):
        list_temp..append(i)

    for b in list_temp:
        if os.path.isdir(path + b):
            folder.append(b)

        if len(suffix_list) == 0:
            lista = list_temp 
        else:
            for b in folder:
                if build_entries_list(path + b + "/", suffix_list):
                    lista.append(b)
            for a in list_temp:
                if os.path.splitext(a)[1] in suffix_list:
                    lista.append(a) 
        options = lista + [">back<", ">quit<"]
        selected = pick[options, "Elige:", multi_select=True, min_selection_count=1]
        selected_deal(selected, options, suffix_list, path):
            selected_name =

