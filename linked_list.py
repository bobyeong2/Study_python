# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.10.2
#   kernelspec:
#     display_name: data-anal
#     language: python
#     name: data-anal
# ---

# ##### 하루에 하나씩 구매한 알고리즘 책을 봐가면서 알고리즘을 이해하고 작성하기
#

# - 자료구조 중 연결 리스트구현 (python)

# +
class Node :
    def __init__(self, data, next=None) :
        self.data = data
        self.next = next
        
def init() :
    global node1
    node1 = Node(1)
    
    node2 = Node(2)
    
    node3 = Node(3)
    
    node4 = Node(4)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    
    
def delete(del_data) : 
    global node1
    pre_node = node1
    next_node = pre_node.next
    if pre_node.data == del_data :
        node1 = next_node
        del pre_node
        return
    
    while next_node :
        if next_node.data == del_data :
            pre_node.next = next_node.next
            next_node = next_node.next
            break
        pre_node = next_node
        next_node = next_node.next
            
def insert(ins_data) :
    global node1
    new_node = Node(ins_data)
    new_node.next = node1
    node1 = new_node
    
def print_list() :
    global node1
    node = node1
    while node :
        print(node.data)
        node=node.next
        print()
        


    


# -

init()
insert(10)
insert(3)
delete(10)
print_list()


