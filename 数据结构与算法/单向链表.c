#include <stdio.h>
#include <stdlib.h>

typedef int ElemType;

// 链表存储结构
typedef struct node{
    ElemType data;
    struct node* next;
}Node;

// 初始化链表
Node* initlist() {
    Node *head=(Node*)malloc(sizeof(Node));
    head->data=0;
    head->next=NULL;
    return head;
}

// 在链表头部插入元素
void insertHead(Node *head, ElemType e) {
    Node *p=(Node*)malloc(sizeof(Node));
    p->data=e;
    p->next=head->next;
    head->next=p;
}

// 遍历链表并打印元素
void listNode(Node *head) {
    Node *p=head->next;
    while(p!=NULL) {
        printf("%d ",p->data);
        p=p->next;
    }
    printf("\n");
}

// 获取尾节点
Node* get_tail(Node *head) {
    Node *p=head;
    while(p->next!=NULL) {
        p=p->next;
    }
    return p;
}

// 在链表尾部插入元素
Node* insertTail(Node *tail,ElemType e) {
    Node *p=(Node*)malloc(sizeof(Node));
    p->data=e;
    tail->next=p;
    p->next=NULL;
    return p;
}

// 在指定位置插入元素（position为插入位置，从头指针之后开始计数）
int insertNode(Node *head, int position, ElemType e) {
    Node *p=head; // 指向链表头节点
    int i=0;
    // 遍历链表找到插入位置的前一个节点
    while(i<position-1) {
        p=p->next;
        i++;
        if(p==NULL) {
            printf("插入位置不合法，无法插入元素。\n");
            return 0; // 插入位置不合法
        }
    }
    // 创建新节点并插入
    Node *newNode=(Node*)malloc(sizeof(Node));
    newNode->data=e;
    newNode->next=p->next;
    p->next=newNode;
    return 1; // 成功插入元素
}

// 删除指定位置的节点（position为删除位置，从头指针之后开始计数）
int deletNode(Node *head,int position) {
    Node *p=head;
    int i=0;
    // 遍历链表找到删除位置的前一个节点
    while(i<position-1) {
        p=p->next;
        i++;
        if(p==NULL || p->next==NULL) {
            printf("删除位置不合法，无法删除元素。\n");
            return 0; // 删除位置不合法
        }
    }
    // 删除节点
    Node *q=p->next; // 要删除的节点
    p->next=q->next; // 前一个节点指向要删除节点的下一个节点
    free(q); // 释放要删除的节点
    return 1; // 成功删除元素
}

// 获取链表长度
int listLength(Node *head) {
    Node *p=head; // 把头指针也计算在内
    int len=0;
    while(p!=NULL) {
        len++;
        p=p->next;
    }
    return len;
}

// 释放链表内存
void listFree(Node *head) {
    Node *p=head->next;
    Node *q;
    while(p!=NULL) {
        q=p->next;
        free(p);
        p=q;
    }
    head->next=NULL;
}

int main() {
    Node *head=initlist();
    printf("链表初始化完成。\n");
    
    insertHead(head, 1);
    insertHead(head, 2);
    insertHead(head, 3);
    printf("在链表头部插入元素后，链表中的元素为: ");
    listNode(head);

    Node *tail=get_tail(head);
    tail=insertTail(tail, 4);
    tail=insertTail(tail, 5);
    printf("在链表尾部插入元素后，链表中的元素为: ");
    listNode(head);

    insertNode(head, 3, 6);
    printf("在链表第3个位置插入元素6后，链表中的元素为: ");
    listNode(head);

    deletNode(head, 2);
    printf("删除链表第2个位置的元素后，链表中的元素为: ");
    listNode(head);

    listFree(head);
    return 0;
}
