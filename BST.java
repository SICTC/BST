
public class BST 
{
	private class node
	{
		public Comparable data;
		public node left;
		public node right;
		
		public node(Comparable x)
		{
			data=x;
			left=right=null;
		}
		
		public boolean hasLC()
		{
			return left!=null;
		}
		
		public boolean hasRC()
		{
			return right!=null;
		}
		
		public String toString()
		{
			return data.toString();
		}
	}
	
	private node root;
	private int count;
	
	public BST()
	{
		root=null;
		count=0;
	}
	
	private node insert(Comparable x, node r)
	{
		if(r==null) //found it
		{
			node t=new node(x);
			return t;
		}
		if(x.compareTo(r.data)<0) //less than--go to LC
		{
			r.left = insert(x,r.left);
		}
		else //greater than--go to RC
		{
			r.right = insert(x, r.right);
		}
		
		return r;
	}
	
	public void insert(Comparable x)
	{
		root=insert(x,root);
		count++;
	}
	
	private Comparable lookup(Comparable x, node n)
	{
		if(n==null)
		{
			return null;
		}
		if(x.compareTo(n.data)==0) //found it!
		{
			return n.data;
		}
		if(x.compareTo(n.data)<0) //less than--check left branch
		{
			return lookup(x,n.left);
		}
		else //greater than--check right branch
		{
			return lookup(x,n.right);
		}
	}
	
	public Comparable lookup(Comparable x)
	{
		return lookup(x, root);
	}
	
	private Comparable min(node n)
	{
		if(n==null)
		{
			return null;
		}
		if(n.left==null)
		{
			return n.data;
		}
		return min(n.left);
	}
	
	public Comparable getMin()
	{
		return min(root);
	}
	
	public static final int PRE=-1;
	public static final int IN=0;
	public static final int POST=1;
	
	private void traverse(node n, int order, String seperator)
	{
		if(order==PRE)
		{
			System.out.print(n + seperator);
		}
		if(n.hasLC())
		{
			traverse(n.left, order, seperator);
		}
		if(order==IN)
		{
			System.out.print(n + seperator);
		}
		if(n.hasRC())
		{
			traverse(n.right, order, seperator);
		}
		if(order==POST)
		{
			System.out.print(n + seperator);
		}
	}
	
	public void traverse(int order, String seperator)
	{
		if(root==null)
		{
			System.out.println("Empty!");
		}
		else
		{
			traverse(root, order, seperator);
		}
	}
	

	
}
