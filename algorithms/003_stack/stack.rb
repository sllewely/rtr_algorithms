# sllewelyn

class Stack
  def push(val)
    node = Node.new(val)
    if is_empty?
      @last = node
    else
      node.prev = @last
      @last = node
    end
  end

  def pop
    return if is_empty?
    output = @last
    @last = @last.prev
    output.val
  end

  def is_empty?
    @last.nil?
  end
end

class Node
  attr_accessor :prev, :val

  def initialize(val)
    @val = val
  end
end


# Example reverse a string

stack = Stack.new
str = 'alphabet'
rstr = ''
str.chars.each { |c| stack.push(c) }
while !stack.is_empty?
  rstr = stack.pop
  puts rstr
end

puts rstr
