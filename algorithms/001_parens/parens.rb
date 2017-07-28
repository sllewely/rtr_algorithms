# parens july 2017

sample = "(()))("

def valid_parens?(str)
  count = 0
  str.chars.each do |chr|
    if chr == '('
      count += 1
    elsif chr == ')'
      count -= 1
    end
    return false if count < 0
  end
  count == 0
end

puts sample
puts valid_parens?(sample)

sample = "((aklsfel))"
puts sample
puts valid_parens?(sample)

