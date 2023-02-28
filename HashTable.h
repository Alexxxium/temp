#pragma once
#include <list>
#include <string>


struct Node
{
	int key;
	std::string value;

	explicit Node(const int &k, const std::string &vl): key(k), value(vl) {}

	Node(const Node &node): key(node.key), value(node.value) {}

	void operator=(const Node &node) {
		key = node.key;
		value = node.value;
	}

	bool operator== (const int &vl)     const { return key == vl; }
	auto operator<=>(const int &vl)     const { return key <=> vl; }
	bool operator== (const Node &node)  const { return key == node.key; }
	auto operator<=>(const Node &node)  const { return key <=> node.key; }
};


class HashTable
{
private:

	typedef std::list<Node*> List;

	static int defailtCapacity;
	static float redistCoeff;

	size_t capacity, count;

	List *array;

	size_t Hash(const Node *node) const;
	size_t Hash(const int &key)   const;

	void DestroyArray(List*);

	void reHash (const List*, const size_t);
	void reWrite(const List*);

public:

	explicit HashTable(int cpcty = defailtCapacity);
	HashTable(const HashTable&);

	void operator=(const HashTable&);

	~HashTable()  { DestroyArray(array); }
	size_t size() { return count; }

	HashTable::List::iterator find(const int&) const;
	void reserve(const int);
	void insert (const int&, const std::string&);
	void erase  (const int&);
	void clear  ();

	void outTable();
};


int HashTable::defailtCapacity = 10;
float HashTable::redistCoeff = 0.75;


HashTable::HashTable(int cpcty): count(0), capacity(cpcty)
{
	if (cpcty < 0) throw 1;

	array = new std::list<Node*>[capacity];
}
HashTable::HashTable(const HashTable &copy):
	count(copy.count),
	capacity(copy.capacity)
{
	array = new List[capacity];

	reWrite(copy.array);
}

void HashTable::operator=(const HashTable &copy)
{
	if (&copy == this) return;

	count = copy.count;
	capacity = copy.capacity;

	DestroyArray(array);
	array = new List[capacity];

	reWrite(copy.array);
}
void HashTable::DestroyArray(List *arr) 
{
	for (size_t i = 0; i < capacity; ++i)
		for (const auto &it : arr[i])
			delete it;
	delete[] arr;
}


size_t HashTable::Hash(const Node *node) const
{
	return node->key % capacity;
}
size_t HashTable::Hash(const int &key)   const
{
	return key % capacity;
}

void HashTable::reHash  (const List *copy, const size_t lenght)
{
	for (int i = 0; i < lenght; ++i)
		for (const auto &it : copy[i])
			array[Hash(it)].push_back(it);
}
void HashTable::reWrite (const List *copy)
{
	for (int i = 0; i < capacity; ++i)
		for (const auto &it : copy[i])
			array[i].push_back(it);
}
void HashTable::reserve (const int newCapacity)
{
	if (newCapacity <= capacity) return;
	outTable();
	List *tempArr = array;
	size_t tempSz = capacity;

	capacity = newCapacity;
	array = new List[capacity];
	
	reHash(tempArr, tempSz);
}
void HashTable::insert  (const int &key, const std::string &value)
{
	Node *newData = new Node(key, value);
	array[Hash(key)].push_back(newData);
	
	if (++count * 1.0 / capacity >= redistCoeff)
		reserve(capacity * 2);
}
void HashTable::erase   (const int &key)
{
	List &ref = array[Hash(key)];
	auto it = find(key);

	if (it != ref.end()) {
		ref.erase(it);
		--count;
	}	
}
void HashTable::clear   ()
{
	DestroyArray(array);

	array = new List[capacity];
}

HashTable::List::iterator HashTable::find(const int &key) const
{
	List &ref = array[Hash(key)];
	List::iterator it = ref.begin();

	for (it; it != ref.end(); ++it)
		if ((*it)->key == key)
			return it;

	return ref.end();
}

void HashTable::outTable()
{
	for (int i = 0; i < capacity; ++i) {
		for (const auto &it : array[i])
			std::cout << '(' << it->key << " ; " << it->value << ")\t";
		std::cout << std::endl;
	}	
}